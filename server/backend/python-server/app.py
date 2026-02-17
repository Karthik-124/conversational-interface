import flask
import flask_cors
import markdown
import json

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if flask.request.method == "GET":
        content = flask.request.args.get("message", "")
        msg_type = "text"
    else:
        data = flask.request.get_json(silent=True)
        if data:
            msg_type = data.get("type", "text")
            content = data.get("message", "") if msg_type != "poi" else data
        else:
            content = flask.request.data.decode("utf-8")
            msg_type = "text"

    if not content:
        return flask.jsonify({"error": "No message provided"}), 400

    reply = content
    
    if msg_type == "md":
        reply = markdown.markdown(content, extensions=["tables", "fenced_code"])
    elif msg_type == "poi":
        if isinstance(content, dict):
            reply = {
                "locations": content.get("locations", []),
                "zoom": content.get("zoom", 13)
            }
        elif isinstance(content, str):
            try:
                poi_data = json.loads(content)
                reply = {
                    "locations": poi_data.get("locations", []),
                    "zoom": poi_data.get("zoom", 13)
                }
            except:
                msg_type = "text"
                reply = content
    elif msg_type == "choice":
        if isinstance(content, str):
            try:
                choice_data = json.loads(content)
            except:
                choice_data = None
                msg_type = "text"
        else:
            choice_data = content

        if choice_data:
            reply = {
                "text": choice_data.get("text", "Select an option:"),
                "options": choice_data.get("options", [])
            }

    return flask.jsonify({
        "type": msg_type,
        "reply": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

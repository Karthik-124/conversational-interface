import flask
import flask_cors
import markdown
import json
import os

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
            content = data.get("message", "")
        else:
            content = flask.request.data.decode("utf-8")
            msg_type = "text"

    if not content:
        return flask.jsonify({"error": "No message provided"}), 400

    if msg_type == "md":
        reply = markdown.markdown(content, extensions=["tables", "fenced_code"])
    elif msg_type == "choice":
        
        if isinstance(content, str):
            try:
                choice_data = json.loads(content)
            except:
                reply = content
                msg_type = "text"
                choice_data = None
        else:
            choice_data = content
        
        if choice_data:
            reply = json.dumps({
                "question": choice_data.get("question", "Select an option:"),
                "options": choice_data.get("options", [])
            })
    else:
        msg_type = "text"
        reply = content

    return flask.jsonify({
        "type": msg_type,
        "reply": reply
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


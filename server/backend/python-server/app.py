import flask
import flask_cors
import markdown

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
            # User typed valid JSON
            msg_type = data.get("type", "text")
            content = data.get("message", "")
        else:
            # Not JSON → treat entire body as text
            content = flask.request.data.decode("utf-8")
            msg_type = "text"

    if not content:
        return flask.jsonify({"error": "No message provided"}), 400

    if msg_type == "md":
        reply = markdown.markdown(content, extensions=["tables", "fenced_code"])
    else:
        msg_type = "text"
        reply = content

    return flask.jsonify({
        "type": msg_type,
        "reply": reply
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

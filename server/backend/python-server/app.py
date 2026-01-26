from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["GET", "POST"])
def chat():  
    if request.method == "GET":
        message = request.args.get("message", "")
    else:    
        data = request.get_json(silent=True) or {}
        message = data.get("message", "")

    return jsonify({
        "reply": f"{message}"
    })

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify
from chat_handler import handle_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/", methods=["POST"])
def webhook():
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid JSON format"}), 400

        data = request.get_json()
        msg = data.get("message", {}).get("text", "")

        if not msg:
            return jsonify({"error": "No message text found"}), 400

        response = handle_query(msg)
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Set your Gemini API key and endpoint
API_KEY = "AIzaSyBwXgII-HyTHk359ZmFXwPEoMANoPotzEk"  # Replace with your actual API key
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.route("/")
def home():
    return app.send_static_file('index.html')  # This serves the index.html file from the /static folder

@app.route("/chat", methods=["POST"])
def chat():
    # Get user message from the frontend
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({"reply": "No message received!"}), 400

    # Prepare the request payload for the Gemini API
    payload = {
        "contents": [{
            "parts": [{"text": user_message}]
        }]
    }

    try:
        # Send request to Gemini API
        response = requests.post(
            f"{API_ENDPOINT}?key={API_KEY}",
            headers={"Content-Type": "application/json"},
            json=payload
        )

        if response.status_code == 200:
            data = response.json()
            bot_reply = (
                data.get('candidates', [{}])[0]
                    .get('content', {})
                    .get('parts', [{}])[0]
                    .get('text', "No response")
            )
            return jsonify({"reply": bot_reply.strip()})

        else:
            return jsonify({"reply": "Error with the Gemini API!"}), 500

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5500)  # Flask server will run on port 5500

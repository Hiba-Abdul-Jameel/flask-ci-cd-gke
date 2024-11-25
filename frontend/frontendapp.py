from flask import Flask, render_template, jsonify
import requests  # To send requests to the backend

app = Flask(__name__)

# URL of the backend (your existing app running on a specific port)
BACKEND_URL = 'http://localhost:5000/get_messages'  # Adjust if running remotely


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_messages')
def get_messages():
    try:
        # Make a request to the backend to fetch messages
        response = requests.get(BACKEND_URL)
        messages = response.json()  # Convert the response to JSON
        return jsonify(messages)
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching messages: {e}")
        return jsonify({"error": "Failed to fetch messages"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)

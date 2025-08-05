from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, db
import os
import json

# === Gemini Setup ===
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# === Firebase Setup ===
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://feel-leaf-default-rtdb.firebaseio.com/'  # Optional: insert your actual Realtime DB URL
})

# === Flask App ===
app = Flask(__name__)
CORS(app)

# === Gemini Chat Endpoint ===
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    response = chat.send_message(user_input)
    return jsonify({'response': response.text})

# === Emotion → Firebase Update Endpoint ===
@app.route('/emotion', methods=['POST'])
def emotion():
    emotion = request.json['emotion']
    ref = db.reference('/plant_emotion')
    ref.set(emotion)
    return jsonify({'status': 'sent'})
    from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, db
import os
import json

# === Gemini Setup ===
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# === Firebase Setup ===
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://feel-leaf-default-rtdb.firebaseio.com/'  # Optional: insert your actual Realtime DB URL
})

# === Flask App ===
app = Flask(__name__)
CORS(app)

# === Gemini Chat Endpoint ===
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    response = chat.send_message(user_input)
    return jsonify({'response': response.text})

# === Emotion → Firebase Update Endpoint ===
@app.route('/emotion', methods=['POST'])
def emotion():
    emotion = request.json['emotion']
    ref = db.reference('/plant_emotion')
    ref.set(emotion)
    return jsonify({'status': 'sent'})

@app.route('/', methods=['GET'])
def home():
    return "Feel Leaf is awake. Ready to read your vibe 🌿"


# === Run App ===
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)



# === Run App ===
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)



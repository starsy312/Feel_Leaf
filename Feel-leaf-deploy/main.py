from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, db

# === Gemini Setup ===
genai.configure(api_key="AIzaSyA7oKg3QEm1P68y7zzjibW4gWa3oiN1a6s")  # Replace with your real key

# === Firebase Setup ===
cred = credentials.Certificate("firebase_key.json")  # Upload this to Render too
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://feel-leaf-default-rtdb.firebaseio.com/'  # Replace if needed
})

# === Flask App ===
app = Flask(__name__)
CORS(app)

# Gemini Chat Endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    response = chat.send_message(user_input)
    return jsonify({'response': response.text})

# Emotion → Firebase Update
@app.route('/emotion', methods=['POST'])
def emotion():
    emotion = request.json['emotion']
    ref = db.reference('/plant_emotion')
    ref.set(emotion)
    return jsonify({'status': 'sent'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

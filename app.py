import pickle
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# --- 1. CONFIGURATION ---
MODEL_FILE = 'asl_keypoint_model.pkl'

# --- 2. LOAD MODEL ---
if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError(f"Model file not found: {MODEL_FILE}")

with open(MODEL_FILE, 'rb') as f:
    clf = pickle.load(f)

CLASSES = clf.classes_
app = Flask(__name__)
CORS(app) 

# --- 3. NEW: ADD ROUTE FOR THE FRONTEND ---
@app.route('/')
def serve_index():
    """Serves the index.html file from the same directory."""
    return send_from_directory('.', 'index.html')

# --- 4. API ENDPOINT (No changes here) ---
@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives normalized keypoint features (63 elements) from the frontend,
    runs prediction, and returns the predicted class (letter) and confidence.
    """
    try:
        data = request.json
        features = np.array(data['features'], dtype=np.float32).reshape(1, -1)
        
        probas = clf.predict_proba(features)[0]
        pred_index = np.argmax(probas)
        prediction = CLASSES[pred_index]
        confidence = probas[pred_index]
        
        return jsonify({
            'prediction': prediction,
            'confidence': round(confidence * 100, 2), # Return as percentage
            'success': True
        })
    
    except Exception as e:
        print(f"Prediction Error: {e}")
        return jsonify({'error': str(e), 'success': False}), 500


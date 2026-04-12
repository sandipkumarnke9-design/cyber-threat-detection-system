import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request
from detector.detect import predict_threat

# IMPORTANT: Frontend folder path
app = Flask(__name__, template_folder='../Frontend')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        packet_size = int(request.form['packet_size'])
        duration = int(request.form['duration'])
        protocol = request.form['protocol']
        flag = request.form['flag']

        features = {
            "packet_size": packet_size,
            "duration": duration,
            "protocol": protocol,
            "flag": flag
        }

        result = predict_threat(features)

        return render_template('index.html', prediction=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
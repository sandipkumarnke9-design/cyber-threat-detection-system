# 🚀 Cyber Threat Detection System

## 🔍 Overview
This project is a Machine Learning-based Cyber Threat Detection System that analyzes network traffic and detects suspicious activities in real-time. It uses anomaly detection techniques to identify potential cyber threats and generate alerts.

---

## ⚙️ Features
- 🔍 Real-time network traffic monitoring
- 🧠 Machine Learning-based anomaly detection (Random Forest)
- 🌐 Flask-based web GUI for user interaction
- 🚨 Automated alert system for suspicious activity
- 📊 Feature extraction from network packets

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Flask
- Scapy
- Pandas & NumPy

---

## 📁 Project Structure
Cyber Threat Detection System/
│
├── Backend/ # Flask backend
│ └── app.py
│
├── Frontend/ # HTML GUI
│ └── index.html
│
├── detector/ # Threat detection logic
│ ├── detect.py
│ └── alert.py
│
├── model/ # ML model training
│ ├── train_model.py
│ └── model.pkl
│
├── utils/ # Helper functions
│ └── feature_extractor.py
│
├── data/ # Dataset
│ └── network_data.csv

---

## ▶️ How to Run the Project
python Backend/app.py

### 1️⃣ Clone Repository
git clone https://github.com/sandipkumarnke9-design/cyber-threat-detection-system.git
cd cyber-threat-detection-system

## Install Dependencies
pip install -r requirements.txt

## Train Model
cd model
python train_model.py
cd ..

## Run Application
python Backend/app.py

##  Open in Browser
http://127.0.0.1:5000

### 🧪 Test Inputs
# Normal Traffic
Packet Size: 200
Duration: 10
Protocol: TCP
Flag: SF
👉 Output: Normal Traffic
# Suspicious Traffic
Packet Size: 5000
Duration: 0
Protocol: TCP
Flag: REJ
👉 Output: Threat Detected

📸 Demo
<img width="1110" height="756" alt="image" src="https://github.com/user-attachments/assets/73f29bf8-b534-4706-8c9a-85b925ec93e2" />

🔮 Future Enhancements
📊 Dashboard with graphs and analytics
📧 Email/SMS alert system
🌍 Deployment on cloud (Render/AWS)
🤖 Deep Learning model (LSTM)

👨‍💻 Author
Sandip Kumar
GitHub: https://github.com/sandipkumarnke9-design

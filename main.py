from scapy.all import sniff
from utils.feature_extractor import extract_features
from detector.detect import predict_threat

def process_packet(packet):
    try:
        features = extract_features(packet)
        predict_threat(features)
    except Exception as e:
        print("Error:", e)

print("🚀 System Started...")

sniff(prn=process_packet, count=10)
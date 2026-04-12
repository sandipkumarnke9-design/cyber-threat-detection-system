def extract_features(packet):
    return {
        "packet_size": len(packet),
        "duration": 1,
        "protocol": str(packet.proto),
        "flag": "SF"
    }
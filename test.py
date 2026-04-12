from detector.detect import predict_threat

print("---- TEST START ----")

# Normal case
predict_threat({
    "packet_size": 200,
    "duration": 10,
    "protocol": "TCP",
    "flag": "SF"
})

# Attack case
predict_threat({
    "packet_size": 5000,
    "duration": 0,
    "protocol": "TCP",
    "flag": "REJ"
})
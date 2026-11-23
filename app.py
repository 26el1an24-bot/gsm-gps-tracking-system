
from flask import Flask, render_template, jsonify
from datetime import datetime
import random

app = Flask(__name__)

devices = [
    {
        "id": "GPS-001",
        "name": "Vehicle 1",
        "latitude": 19.0760,
        "longitude": 72.8777,
        "speed": 42,
        "status": "Online"
    },
    {
        "id": "GPS-002",
        "name": "Vehicle 2",
        "latitude": 19.0896,
        "longitude": 72.8656,
        "speed": 35,
        "status": "Online"
    },
    {
        "id": "GPS-003",
        "name": "Vehicle 3",
        "latitude": 19.0600,
        "longitude": 72.8900,
        "speed": 0,
        "status": "Stopped"
    }
]

history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/devices")
def get_devices():
    return jsonify(devices)

@app.route("/api/update")
def update_devices():
    for device in devices:
        if device["status"] == "Online":
            device["latitude"] += random.uniform(-0.0005, 0.0005)
            device["longitude"] += random.uniform(-0.0005, 0.0005)
            device["speed"] = random.randint(20, 70)

        history.append({
            "device_id": device["id"],
            "latitude": device["latitude"],
            "longitude": device["longitude"],
            "speed": device["speed"],
            "timestamp": datetime.now().isoformat()
        })

    return jsonify({
        "devices": devices,
        "history": history[-100:],
        "gsm_status": "Connected"
    })

if __name__ == "__main__":
    app.run(debug=True)

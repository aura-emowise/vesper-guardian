# Vesper: Your Silent Guardian - Web Application v2.2 (with Event Log)
import random
import collections
from flask import Flask, render_template, jsonify
from datetime import datetime

# 
event_log = collections.deque(maxlen=10)
last_status = ""

class SensorSimulator:
    def __init__(self):
        self.base_hr = 70; self.base_eda = 0.5
    def get_reading(self):
        hr = self.base_hr + random.uniform(-2, 2) + (15 if random.random() < 0.1 else 0)
        eda = self.base_eda + random.uniform(-0.05, 0.05) + (0.8 if random.random() < 0.1 else 0)
        return {"hr": hr, "eda": max(0.1, eda)}

class VesperCoreAI:
    def __init__(self, history_size=30):
        self.history = collections.deque(maxlen=history_size); self.baseline_hr = None; self.baseline_eda = None
    def establish_baseline(self):
        if len(self.history) < self.history.maxlen: return False
        self.baseline_hr = sum(r['hr'] for r in self.history) / len(self.history)
        self.baseline_eda = sum(r['eda'] for r in self.history) / len(self.history)
        return True
    def analyze(self, reading):
        self.history.append(reading)
        if not self.baseline_hr and not self.establish_baseline(): return {"status": "Calibrating...", "index": 0}
        hr_dev = (reading['hr'] - self.baseline_hr) / self.baseline_hr
        eda_dev = (reading['eda'] - self.baseline_eda) / self.baseline_eda
        index = max(0, min(10, (hr_dev * 0.4 + eda_dev * 0.6) * 10))
        status = "Calm"
        if 3 <= index < 7: status = "Unease"
        elif index >= 7: status = "Distress Alert!"
        return {"status": status, "index": index}

app = Flask(__name__)
sensor = SensorSimulator()
vesper_ai = VesperCoreAI()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    global last_status, event_log
    reading = sensor.get_reading()
    analysis = vesper_ai.analyze(reading)
    
    # 
    current_status = analysis['status']
    if current_status != last_status and "Calibrating" not in current_status:
        timestamp = datetime.now().strftime("%I:%M:%S %p")
        event_log.appendleft(f"{timestamp} - Status changed to {current_status}")
        last_status = current_status
    
    # 
    analysis['log'] = list(event_log)
    return jsonify(analysis)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Vesper: Your Silent Guardian - Web Application Prototype v2.1 (FIXED)
# Enhanced with a proper UI and live updates.

import random
import collections
# 
from flask import Flask, Response, render_template, jsonify

# ---  ---
class SensorSimulator:
    def __init__(self):
        self.base_hr = 70
        self.base_eda = 0.5
    def get_reading(self):
        hr = self.base_hr + random.uniform(-2, 2) + (15 if random.random() < 0.1 else 0)
        eda = self.base_eda + random.uniform(-0.05, 0.05) + (0.8 if random.random() < 0.1 else 0)
        return {"hr": hr, "eda": max(0.1, eda)}

class VesperCoreAI:
    def __init__(self, history_size=30):
        self.history = collections.deque(maxlen=history_size)
        self.baseline_hr = None
        self.baseline_eda = None
    def establish_baseline(self):
        if len(self.history) < self.history.maxlen: return False
        sum_hr = sum(r['hr'] for r in self.history); self.baseline_hr = sum_hr / len(self.history)
        sum_eda = sum(r['eda'] for r in self.history); self.baseline_eda = sum_eda / len(self.history)
        return True
    def analyze(self, reading):
        self.history.append(reading)
        if not self.baseline_hr and not self.establish_baseline():
            return {"status": "Calibrating...", "index": 0}
        hr_deviation = (reading['hr'] - self.baseline_hr) / self.baseline_hr
        eda_deviation = (reading['eda'] - self.baseline_eda) / self.baseline_eda
        wellbeing_index = max(0, min(10, (hr_deviation * 0.4 + eda_deviation * 0.6) * 10))
        status = "Calm"
        if 3 <= wellbeing_index < 7: status = "Unease"
        elif wellbeing_index >= 7: status = "Distress Alert!"
        return {"status": status, "index": wellbeing_index}
# -- ---

# 
app = Flask(__name__)
sensor = SensorSimulator()
vesper_ai = VesperCoreAI()

# 
@app.route("/")
def index():
    # 
    return render_template("index.html")

# 
@app.route("/data")
def data():
    reading = sensor.get_reading()
    analysis = vesper_ai.analyze(reading)
    return jsonify(analysis)

# 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
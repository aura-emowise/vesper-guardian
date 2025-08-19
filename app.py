# Vesper: Your Silent Guardian - v3.0 (Full Dashboard)
import random
import collections
from flask import Flask, render_template, jsonify
from datetime import datetime

# ---  ---
PATIENT_INFO = {
    "name": "John Doe",
    "year_of_birth": 1957,
    "height_cm": 182,
    "weight_kg": 115,
    "anamnesis": "Diabetes II, Appendectomy (2010)"
}

event_log = collections.deque(maxlen=10)
last_status = ""

# ---  ---
class SensorSimulator:
    def __init__(self):
        self.base_hr = 70
        self.base_eda = 0.5
        self.base_bp_systolic = 120
        self.base_bp_diastolic = 80

    def get_reading(self):
        # ---
        is_event = random.random() < 0.1
        
        # --
        hr = self.base_hr + random.uniform(-2, 2) + (15 if is_event else 0)
        eda = self.base_eda + random.uniform(-0.05, 0.05) + (0.8 if is_event else 0)
        bp_s = self.base_bp_systolic + random.uniform(-5, 5) + (20 if is_event else 0)
        bp_d = self.base_bp_diastolic + random.uniform(-3, 3) + (10 if is_event else 0)
        
        return {
            "hr": hr, 
            "eda": max(0.1, eda),
            "bp": f"{int(bp_s)}/{int(bp_d)}"
        }

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

# --- Flask  ---
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
    
    current_status = analysis['status']
    if current_status != last_status and "Calibrating" not in current_status:
        timestamp = datetime.now().strftime("%I:%M:%S %p")
        event_log.appendleft(f"{timestamp} - Status changed to {current_status}")
        last_status = current_status
    
    # --
    response_data = {
        "analysis": analysis,
        "vitals": reading,
        "patient_info": PATIENT_INFO,
        "log": list(event_log)
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Vesper: Your Silent Guardian

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A Medi-Hacks submission to bridge the communication gap in caregiving through an AI-powered non-verbal distress monitor.**

![Vesper Dashboard Screenshot](https://i.imgur.com/r6s8y5H.png)
*(Note: This is a placeholder image. You should take a screenshot of your final, working application and replace the URL)*

### Live Demo
**[https://vesper-guardian.onrender.com](https://vesper-guardian.onrender.com)**

## The Problem

Millions of people act as caregivers for loved ones who cannot verbally express their needs—whether it's an elderly parent with dementia, a post-surgery patient, or a non-verbal child. This creates a constant state of anxiety for the caregiver and risks delayed care for the patient. We are forced to guess, "Are they okay right now?"

## Our Solution: Vesper

Vesper is a silent guardian. It's an interactive dashboard that translates raw physiological data from a wearable sensor into a simple, actionable **Well-being Index**. Instead of showing confusing graphs, Vesper provides an intuitive, color-coded status: **Calm, Unease, or Distress Alert!**

But Vesper is more than just a monitor; it's a **collaborative learning system**. It closes the feedback loop between the AI and the human caregiver, transforming a passive monitoring experience into an active, intelligent partnership.

## The Core Concept: From INTI to Vesper

This prototype is the first practical application of our broader concept, **INTI (Artificial Neural Creative Intelligence)**. The core idea of INTI is that a truly empathetic AI must learn from the full spectrum of human emotional and physiological experience over time.

Vesper implements the first crucial step of this vision: **contextual data logging**. By allowing caregivers to log real-world events, we begin building the unique dataset needed to train an AI that doesn't just recognize distress, but truly *understands* its context.

## Key Features

### 1. Real-Time Monitoring
*   **Live Vitals:** Simulates real-time data streaming for Heart Rate (HR), Electrodermal Activity (EDA), and Blood Pressure (BP).
*   **Well-being Index:** An AI-analyzed score from 0 to 10 that provides an at-a-glance summary of the patient's state.
*   **Color-Coded Status:** The entire UI intuitively shifts color (green, amber, red) to reflect the current status, with a pulsing animation for critical alerts.

### 2. Interactive Caregiver Tools
*   **"Log Event" Functionality:** The caregiver can open a modal to add crucial context to the data timeline.
*   **Contextual Scenarios:** Pre-defined buttons like "Medication Given," "Patient Repositioned," and "Family Visit" teach the AI to differentiate between medical events, physical movements, and social interactions.
*   **"Acknowledge Alert" Button:** Appears during alerts, allowing the caregiver to confirm they have seen the issue and are responding. This validates the AI's detection.

### 3. Intelligent Event Logging
*   **Smart Timeline:** The "Recent Events" log clearly displays a history of status changes and manual entries.
*   **Source-Based Classification:** Events are tagged by their source—`AI` (status change), `Manual` (caregiver input), or `System`—providing a rich, analyzable history of patient-caregiver-AI interactions.

## Technology Stack

*   **Backend:** Python 3, Flask
*   **Frontend:** HTML5, CSS3 (Grid Layout), Vanilla JavaScript (ES6)
*   **Deployment:** Render, Git/GitHub

## Local Setup & Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```    git clone https://github.com/aura-emowise/vesper-guardian.git
    cd vesper-guardian
    ```

2.  **Create and activate a virtual environment:**
    ```
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Future Vision

This prototype is the foundation. With the contextual data gathered by Vesper, future versions could:
*   **Develop predictive models** to anticipate distress events *before* they become critical.
*   **Analyze the effectiveness** of different interventions (e.g., how quickly a specific medication improves the patient's state).
*   **Integrate with smart home devices** to automatically adjust the patient's environment (e.g., dimming lights or playing calming music when stress is detected).

---
*Built with care for Medi-Hacks.*```
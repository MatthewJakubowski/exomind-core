<div align="center">
  <img src="https://raw.githubusercontent.com/MatthewJakubowski/Universal-Lab-Converter/main/going_dark_cover.jpg" width="100%" alt="System Status: Going Dark. Deep Work Protocol.">
</div>

# 🧬 EXOMIND-CORE v2.0

**Personal Biometric Assistant & Expert System (Android/Python)**

ExoMind is a modular bio-feedback system designed for mobile devices running within the Pydroid 3 environment. The application analyzes physiological parameters (heart rate) in the context of the circadian cycle (Work/Sleep/Recovery), providing real-time instructions to optimize operator performance.

---

## 🛡️ Architecture Philosophy: "Offline First"

This project is built upon two core principles: **Data Security** and **Fault Tolerance**.

### 1. Security & API Keys (Air-gapped Logic)
We have consciously opted out of a default cloud connection (Google Gemini/OpenAI).
* **Reasoning:** An API Key is equivalent to a credit card. We do not expose sensitive keys in public repositories.
* **Solution:** By default, the system utilizes a local `cortex.py` module (Expert System). It is free, private, and operates entirely offline.
* **AI Option:** For users with their own keys, a `cortex_ai.py` module is included (activation instructions below).

### 2. Hardware Simulation (Virtual Actuator)
Modern Android versions often restrict direct hardware access (Vibration/TTS) for Python scripts.
* **Solution:** We implemented an intelligent bridge: `actuators.py`.
* **Mechanism:** The system automatically detects the presence of the `android-helper` library.
    * **✅ Hardware Mode:** If the library is found – the phone vibrates and speaks.
    * **⚠️ Virtual Mode:** If the library is missing – the system seamlessly transitions to simulation mode, displaying alerts in the console (`[VIBRATION]: BZZZZ!`). This ensures the app never crashes due to environment errors.

---

## 📂 System Structure

* **`main.py`** – Operational Brain. Manages the time loop and decision logic.
* **`actuators.py`** – Nervous System. Hybrid driver (Handles both physical haptics and text simulation).
* **`cortex.py`** – **[DEFAULT]** Local knowledge base for psychology and physiology.
* **`cortex_ai.py`** – **[OPTIONAL]** Integration module for Google Gemini (requires configuration).
* **`dashboard.py`** – Analytics Module. Generates daily reports and performance charts.
* **`bio_history.csv`** – Long-term memory (auto-generated).

---

## 🚀 Usage Instructions

### Requirements
* Android Device.
* **Pydroid 3** app (available on Google Play).

### Quick Start
1.  Download the files to a folder on your device.
2.  Open `main.py` in Pydroid 3.
3.  Run the script. The system will request heart rate input and make a decision.
4.  To view the daily summary, run `dashboard.py`.

---

## 🔧 Advanced Configuration (For Developers)

### Path A: Enabling Vibration & Voice (Hardware)
If you want physical feedback:
1.  In Pydroid, go to `PIP` -> `Install`.
2.  **Uncheck** "Use prebuilt libraries repository".
3.  Install library: `android-helper`.
4.  (Optional) Install "Pydroid permissions plugin" from the Play Store.
*The system will auto-detect this change upon the next restart.*

### Path B: Enabling AI (LLM)
If you wish to harness the power of Gemini Pro:
1.  Generate your own API Key via Google AI Studio.
2.  In `main.py`, change the import line:
    `from cortex import Brain` --> `from cortex_ai import Brain`
3.  In `cortex_ai.py`, configure the `GOOGLE_API_KEY` environment variable.
    *(Warning: Never hardcode your key directly into the file if you plan to publish the code!)*

---

## 🤝 Acknowledgments

**Co-architected with Google Gemini.**
This project was developed with the active assistance of Artificial Intelligence. Gemini acted as a technical thought partner, assisting with debugging, architectural decisions, and the implementation of the "Virtual Actuator" logic during critical development phases.

---

## ⚠️ Disclaimer
This software is for educational and experimental purposes ("Hobbyist Bio-hacking"). It is not a medical device. The author is not responsible for health decisions made based on system suggestions.

---
*Copyright © 2026 Mateusz Jakubowski | MIT License*

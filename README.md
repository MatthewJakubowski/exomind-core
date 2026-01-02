# 🧬 EXOMIND-CORE v3.0 Ultimate

**Personal Biometric Assistant & Holistic Health Record (Android/Python)**

ExoMind is a modular bio-feedback system designed for mobile devices running within the Pydroid 3 environment. Version 3.0 expands beyond simple heart rate monitoring to become a comprehensive, offline health database.

---

## 🔥 v3.0: The "Ultimate" Update
This version introduces a **Holistic Database** capable of tracking 20+ physiological parameters.

### 🏥 Manual Health Bridge (Samsung Health / Lab Results)
Due to Android security sandboxing, direct API access to Samsung Health is restricted for Python scripts.
ExoMind v3.0 bypasses this via the **Manual Entry Protocol**:
* **Morning Report:** Input Sleep Score, Energy Score, and HRV (from your watch).
* **Lab Mode:** Archive blood test results (Vitamin D3, Cortisol, Glucose, etc.).
* **Quick Check:** Standard Heart Rate monitoring.

**All data remains 100% offline in a local CSV file (`bio_history_ultimate.csv`).**

---

## 🛡️ Architecture Philosophy: "Offline First"

This project is built upon two core principles: **Data Security** and **Fault Tolerance**.

### 1. Security & API Keys
We do not expose sensitive API keys. By default, the system utilizes a local `cortex.py` (Expert System).
* **AI Option:** For users with their own keys, a `cortex_ai.py` module is included (Gemini integration).

### 2. Hardware Simulation (Virtual Actuator)
We implemented an intelligent bridge: `actuators.py`.
* **✅ Hardware Mode:** If `android-helper` library is found – the phone vibrates/speaks.
* **⚠️ Virtual Mode:** If missing – the system transitions to text simulation.

---

## 📂 System Structure

* **`main.py`** – **[UPDATED]** Core logic now supports multi-parameter data entry (Energy, Stress, Lab results).
* **`dashboard.py`** – **[UPDATED]** Analytics module now visualizes correlations (e.g., Heart Rate vs. Energy Score).
* **`actuators.py`** – Nervous System (Hybrid driver).
* **`cortex.py`** – Local knowledge base.
* **`bio_history_ultimate.csv`** – The expanded database file.

---

## 🚀 Usage Instructions

1.  Open `main.py` in Pydroid 3.
2.  Choose your mode:
    * `1` - Quick Heart Rate Check.
    * `2` - Morning Report (Samsung Health Data).
    * `3` - Lab Results Entry.
3.  To view the charts, run `dashboard.py`.

---

## 🤝 Acknowledgments

**Co-architected with Google Gemini.**
This project was developed with the active assistance of Artificial Intelligence, acting as a technical thought partner in designing the modular architecture and the manual data bridging protocol.

---
*Copyright © 2026 Mateusz Jakubowski | MIT License*

<div align="center">
  <img src="https://raw.githubusercontent.com/MatthewJakubowski/Universal-Lab-Converter/main/going_dark_cover.jpg" width="100%" alt="System Status: Going Dark. Deep Work Protocol.">
</div>

# 🧬 EXOMIND-CORE v4.0: Connected Omni-Tool

**The Ultimate Open-Source Biometric Assistant Framework (Python/Android)**

ExoMind v4.0 represents the evolution from a simple script to a comprehensive, modular framework. It allows users to track holistic health data, integrate with Artificial Intelligence, and control Smart Home devices—all from a secure, offline-first foundation running on Pydroid 3.

---

## 🏗️ Modular Architecture

The system is designed with a "Choose Your Adventure" philosophy. You decide which modules to activate based on your privacy needs and available hardware.

| Module | Filename | Status | Function |
| :--- | :--- | :--- | :--- |
| **CORE** | `main.py` | ✅ Active | Central logic, time loops, manual data entry. |
| **BIO-DB** | `bio_history_ultimate.csv` | ✅ Active | Encrypted-like local storage for 20+ health metrics. |
| **VISUAL** | `dashboard.py` | ✅ Active | Data analytics & Dual-Axis charting. |
| **HAPTICS**| `actuators.py` | 🔄 Hybrid | Hardware vibration (if available) or Virtual Simulation. |
| **AI** | `cortex_ai.py` | ⏸️ Optional | Google Gemini LLM Integration (Requires API Key). |
| **IoT** | `smarthome.py` | ⏸️ Optional | Samsung SmartThings Bridge (Requires Token). |

---

## 🚀 EXPANSION PACKS (How-To Guide)

### 📦 Pack A: Holistic Health (Standard)
*No internet required. Privacy: 100%.*
The v4.0 Core allows for the manual bridging of data from closed ecosystems (Samsung Health, Garmin) into your open Python database.
1.  Run `main.py`.
2.  Select **Option 2 (Morning Report)** to log Sleep Score, Energy Score, and HRV.
3.  Select **Option 3 (Lab Results)** to archive blood work (Vitamin D3, Cortisol, etc.).
4.  Run `dashboard.py` to see correlations (e.g., *Does low sleep correlate with high heart rate?*).

### 🧠 Pack B: Artificial Intelligence (Gemini)
*Requires Internet. Privacy: Cloud-based.*
Unlocks a psych-physio coach that analyzes your data and gives advice.
1.  Get an API Key from [Google AI Studio](https://aistudio.google.com/).
2.  In `main.py`, switch imports:
    ```python
    # from cortex import Brain       <-- Comment this out
    from cortex_ai import Brain    <-- Uncomment this
    ```
3.  Set your key in environment variables (or secure storage).
4.  Restart. The system now "thinks" before speaking.

### 🏠 Pack C: Smart Home Automation (IoT)
*Requires Internet + Samsung Account.*
Connects your biology to your environment (e.g., dim lights when stress is high).
1.  Get a Personal Access Token from [Samsung SmartThings](https://account.smartthings.com/tokens).
2.  Open `smarthome.py` and input your token (securely).
3.  Run the script directly to **Scan your network** and get Device IDs.
4.  (Advanced) Import `SmartHomeHub` into `main.py` to trigger actions based on heart rate:
    ```python
    if stress_detected:
        hub.control_device(LIGHT_ID, "switch", "off")
    ```

---

## 🛡️ Ironclad Disclaimer & Liability

### 🇺🇸 English (Legal Binding)
**THIS SOFTWARE IS NOT A MEDICAL DEVICE.**
1.  **No Medical Advice:** The ExoMind system is provided solely for **educational, experimental, and bio-hacking purposes**. It is NOT intended to diagnose, treat, cure, or prevent any disease.
2.  **Accuracy Warning:** Data collected via manual input or phone sensors may be inaccurate.
3.  **AI Hallucinations:** AI modules may generate incorrect or dangerous health advice.
4.  **Use at Own Risk:** The author (Mateusz Jakubowski) accepts **NO LIABILITY** for any injury or damage resulting from the use of this code.

### 🇵🇱 Polski (Informacja)
**TO OPROGRAMOWANIE NIE JEST WYROBEM MEDYCZNYM.**
System służy wyłącznie celom edukacyjnym. Autor nie ponosi odpowiedzialności za decyzje zdrowotne podejmowane na podstawie działania programu. Moduły AI i IoT używasz na własną odpowiedzialność.

---

## 🤝 Acknowledgments
**Co-architected with Google Gemini.**
Developed with the active assistance of AI, serving as a technical thought partner in designing the modular architecture, virtual actuators, and the "Manual Bridge" data protocol.

---
*Copyright © 2026 Mateusz Jakubowski | MIT License*

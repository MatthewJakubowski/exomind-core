# PLIK: actuators.py
# MODUŁ: Interfejs Fizyczny (Hardware Bridge)

import time

class BioInterface:
    def __init__(self):
        self.engine = None
        self.mode = "VIRTUAL"
        
        # Próba połączenia z hardwarem (android-helper)
        try:
            import androidhelper
            self.engine = androidhelper.Android()
            self.mode = "HARDWARE"
        except ImportError:
            self.mode = "VIRTUAL"

    def send_alert(self, message):
        """Wysyła silny ALARM (Głos + Wibracja)"""
        if self.mode == "HARDWARE":
            try:
                self.engine.vibrate(500)
                time.sleep(0.2)
                self.engine.vibrate(500)
                self.engine.ttsSpeak(message)
                self.engine.makeToast(f"ALERT: {message}")
            except: pass
        else:
            print(f"\n📢 [GŁOS]: {message}")
            print(f"📳 [WIBRACJA]: BZZZZ! BZZZZ!\n")

    def send_notification(self, message):
        if self.mode == "HARDWARE":
            try:
                self.engine.makeToast(message)
            except: pass
        else:
            print(f"ℹ️ [INFO]: {message}")

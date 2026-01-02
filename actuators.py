# PLIK: actuators.py
# MODUŁ: Interfejs Fizyczny (Hardware Bridge)
# STATUS: Hybrid (Auto-detection)

import time

class BioInterface:
    def __init__(self):
        self.engine = None
        self.mode = "VIRTUAL"
        
        print("--- [INIT] Ładowanie sterowników... ---")
        
        # Próba połączenia z hardwarem (android-helper)
        try:
            import androidhelper
            self.engine = androidhelper.Android()
            self.mode = "HARDWARE"
            print("✅ STEROWNIK: ANDROID (SL4A) - Aktywny")
            # Krótka wibracja na start
            try:
                self.engine.vibrate(200)
            except: pass
        except ImportError:
            print("⚠️ STEROWNIK: BRAK (Tryb Wirtualny)")
            print("-> System działa w trybie bezpiecznym (Symulacja).")
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
            # Wersja tekstowa (Gdy brak sterownika)
            print(f"\n📢 [GŁOS]: {message}")
            print(f"📳 [WIBRACJA]: BZZZZ! BZZZZ!\n")

    def send_notification(self, message):
        """Wysyła łagodne powiadomienie"""
        if self.mode == "HARDWARE":
            try:
                self.engine.makeToast(message)
                self.engine.vibrate(200)
            except: pass
        else:
            print(f"ℹ️ [INFO]: {message}")

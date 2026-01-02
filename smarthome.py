# PLIK: smarthome.py
# MODUŁ: ExoHome (Samsung SmartThings Integration)
# WERSJA: 1.0 Beta
# WYMAGA: pip install requests

import requests
import os
import json

class SmartHomeHub:
    def __init__(self):
        print("--- 🏠 EXOHOME: INICJALIZACJA MODUŁU IOT ---")
        
        # Token powinien być w zmiennych środowiskowych dla bezpieczeństwa
        # W Pydroid można go też wpisać tu testowo (ale nie commituj tego!)
        self.token = os.getenv("SMARTTHINGS_TOKEN")
        
        self.api_url = "https://api.smartthings.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        if not self.token:
            print("⚠️ IOT STATUS: OFFLINE (Brak tokenu SmartThings)")
            print("-> Moduł działa w trybie symulacji.")
            self.mode = "SIMULATION"
        else:
            self.mode = "ONLINE"
            print("✅ IOT STATUS: ONLINE (Połączono z chmurą Samsung)")

    def list_devices(self):
        """Skanuje dom i wypisuje ID wszystkich urządzeń"""
        if self.mode == "SIMULATION":
            print("[SIM] Skanowanie sieci... Znaleziono 0 urządzeń.")
            return

        print("\n🔍 SKANOWANIE URZĄDZEŃ SMARTTHINGS...")
        try:
            response = requests.get(f"{self.api_url}/devices", headers=self.headers)
            if response.status_code == 200:
                devices = response.json().get('items', [])
                for d in devices:
                    print(f"📦 NAZWA: {d.get('label') or d.get('name')}")
                    print(f"   ID: {d.get('deviceId')}")
                    print(f"   TYP: {d.get('components', [{}])[0].get('categories', [{'name':'?'}])[0]['name']}")
                    print("-" * 30)
            else:
                print(f"❌ Błąd API: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Błąd połączenia: {e}")

    def control_device(self, device_id, capability, command, argument=None):
        """
        Uniwersalna funkcja sterująca.
        capability: 'switch', 'switchLevel', 'audioVolume'
        command: 'on', 'off', 'setLevel', 'setVolume'
        """
        if self.mode == "SIMULATION":
            print(f"💡 [SIM] Urządzenie {device_id} -> {command.upper()} ({argument if argument else ''})")
            return

        payload = {
            "commands": [{
                "component": "main",
                "capability": capability,
                "command": command,
                "arguments": [argument] if argument is not None else []
            }]
        }
        
        try:
            url = f"{self.api_url}/devices/{device_id}/commands"
            r = requests.post(url, headers=self.headers, json=payload)
            if r.status_code == 200:
                print(f"⚡ SUKCES: Wysłano komendę {command.upper()}")
            else:
                print(f"⚠️ BŁĄD: {r.text}")
        except Exception as e:
            print(f"❌ Wyjątek sieciowy: {e}")

# --- SEKCJA TESTOWA ---
if __name__ == "__main__":
    # Instrukcja dla użytkownika uruchamiającego plik bezpośrednio
    print("Uruchomiono moduł SmartHome bezpośrednio.")
    hub = SmartHomeHub()
    hub.list_devices()
    
    # PRZYKŁAD UŻYCIA (Dla deweloperów):
    # hub.control_device("ID_TWOJEJ_LAMPY", "switch", "on")
    # hub.control_device("ID_TWOJEJ_LAMPY", "switchLevel", "setLevel", 50)

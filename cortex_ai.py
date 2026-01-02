# PLIK: cortex_ai.py
# MODUŁ: Chmura Obliczeniowa (Google Gemini)
# STATUS: Opcjonalny / Wymaga API Key

import os

class Brain:
    def __init__(self):
        print("--- ☁️ INICJALIZACJA MODUŁU AI (GEMINI) ---")
        try:
            import google.generativeai as genai
            
            # Bezpieczne pobieranie klucza ze zmiennych środowiskowych
            self.api_key = os.getenv("GOOGLE_API_KEY") 
            
            if not self.api_key:
                print("⚠️ INFO: Brak klucza API w zmiennych środowiskowych.")
                print("-> Moduł działa w trybie pasywnym (Offline fallback).")
                self.mode = "OFFLINE"
            else:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-pro')
                self.mode = "ONLINE"
                print("✅ POŁĄCZONO Z CHMURĄ.")
                
        except ImportError:
            print("❌ Brak biblioteki 'google-generativeai'.")
            self.mode = "OFFLINE"

    def analizuj(self, tetno, faza):
        # Fallback do trybu offline, jeśli brak klucza
        if self.mode == "OFFLINE":
            return "TRYB AWARYJNY", "AI niedostępne (Brak klucza/biblioteki)."

        # Prompt inżynieryjny
        prompt = f"""
        Jesteś moim osobistym trenerem biometrycznym.
        Moje dane: Faza dnia: {faza}, Tętno: {tetno} BPM.
        Oceń ten stan jednym, krótkim, żołnierskim zdaniem (max 10 słów). 
        Daj konkretną instrukcję co mam zrobić.
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Zwracamy tuple (prefix, treść)
            return "AI_ADVICE", response.text.strip()
        except Exception:
            return "BŁĄD SIECI", "Nie udało się pobrać porady."

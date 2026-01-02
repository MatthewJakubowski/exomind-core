# PLIK: cortex.py
# MODUŁ: Lokalna Baza Wiedzy

import random

class Brain:
    def __init__(self):
        self.rady_stres = [
            "Wykryto kortyzol. Wykonaj 4 głębokie oddechy.",
            "Zwolnij. Nic nie jest ważniejsze od homeostazy.",
            "Wypij szklankę wody."
        ]
        self.rady_sen = ["Ekran stop. Czas na regenerację.", "Melatonina wymagana."]
        self.rady_flow = ["Utrzymaj ten stan.", "Pełna synchronizacja."]
        self.rady_regeneracja = ["Usiądź. Pozwól sercu zwolnić."]

    def analizuj(self, tetno, faza):
        if faza == "SLEEP" and tetno > 80:
            return "ALARM", random.choice(self.rady_sen)
        elif faza == "WORK":
            if tetno > 110: return "STRES", random.choice(self.rady_stres)
            elif tetno < 60: return "SENNOSC", "Wstań i zrób 10 przysiadów."
            else: return "FLOW", random.choice(self.rady_flow)
        elif faza == "RECOVERY" and tetno > 100:
            return "REGENERACJA", random.choice(self.rady_regeneracja)
        return None, "NORMA"

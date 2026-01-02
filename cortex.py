# PLIK: cortex.py
# MODUŁ: Lokalna Baza Wiedzy (System Ekspercki)
# STATUS: OFFLINE (Prywatny)

import random

class Brain:
    def __init__(self):
        # BAZA WIEDZY
        self.rady_stres = [
            "Wykryto kortyzol. Wykonaj 4 głębokie oddechy (Box Breathing).",
            "System przeciążony. Wyjdź na zewnątrz i spójrz w dal.",
            "Alert. Twój układ nerwowy płonie. Zamknij oczy na 60 sekund.",
            "Zwolnij. Nic nie jest ważniejsze od homeostazy.",
            "Wypij szklankę wody. Odwodnienie wzmaga stres."
        ]
        
        self.rady_sen = [
            "Natychmiast przerwij aktywność. Melatonina wymagana.",
            "Ekran stop. To jest czas na regenerację.",
            "Jeśli nie zaśniesz teraz, jutrzejsza wydajność spadnie o 40%.",
            "Koszmar? To tylko symulacja mózgu. Jesteś bezpieczny."
        ]
        
        self.rady_flow = [
            "Jesteś w strefie. Utrzymaj ten stan.",
            "Parametry idealne. Nie rozpraszaj się.",
            "Pełna synchronizacja. Koduj dalej.",
            "Moc obliczeniowa mózgu na 100%. Wykorzystaj to."
        ]
        
        self.rady_regeneracja = [
            "Tętno za wysokie jak na odpoczynek. Leżysz czy biegniesz?",
            "Usiądź. Pozwól sercu zwolnić.",
            "Zrób skan ciała. Gdzie czujesz napięcie? Puść je."
        ]

    def analizuj(self, tetno, faza):
        """Wybiera odpowiednią poradę bazując na danych."""
        wybrana_rada = ""
        prefix = "NORMA"
        
        if faza == "SLEEP" and tetno > 80:
            wybrana_rada = random.choice(self.rady_sen)
            prefix = "ALARM NOCNY"
            
        elif faza == "WORK":
            if tetno > 110:
                wybrana_rada = random.choice(self.rady_stres)
                prefix = "STRES"
            elif tetno < 60:
                wybrana_rada = "Wstań i zrób 10 przysiadów. Pobudka!"
                prefix = "SENNOSC"
            else:
                wybrana_rada = random.choice(self.rady_flow)
                prefix = "FLOW"
                
        elif faza == "RECOVERY" and tetno > 100:
            wybrana_rada = random.choice(self.rady_regeneracja)
            prefix = "REGENERACJA"
        else:
            return None, "NORMA"

        return prefix, wybrana_rada

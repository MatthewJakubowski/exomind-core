# PLIK: main.py
# SYSTEM EXOMIND v3.0 (ULTIMATE DATABASE)
# Opis: Obsługa danych manualnych (Samsung Health + Lab)

import time
from datetime import datetime
from actuators import BioInterface
from cortex import Brain

# Nowa nazwa pliku bazy (żeby nie mieszać ze starym formatem)
PLIK_PAMIECI = "bio_history_ultimate.csv"

print("--- 🧬 EXOMIND v3.0 ULTIMATE ONLINE 🧬 ---")

interfejs = BioInterface()
mozg = Brain()

# DEFINICJA STRUKTURY DANYCH (16 Kolumn)
NAGLOWKI = [
    "DATA", "GODZINA", "FAZA", "TETNO", "STATUS", 
    "ENERGIA_SCORE", "SEN_H", "STRES_LVL", "KROKI", 
    "CUKIER", "CISNIENIE", "SPO2", "NASTROJ", 
    "LAB_WIT_D3", "LAB_KORTYZOL", "SUPLEMENTACJA"
]

# Inicjalizacja pliku z nagłówkami
try:
    with open(PLIK_PAMIECI, "x") as f:
        f.write(",".join(NAGLOWKI) + "\n")
except FileExistsError:
    pass 

def pobierz_input(tekst, domyslny="-"):
    """Pomocnik do zbierania danych opcjonalnych"""
    val = input(f">> {tekst} (Enter by pominąć): ")
    return val if val else domyslny

while True:
    print("\n" + "="*40)
    print("WYBIERZ TRYB OPERACYJNY:")
    print("1. ⚡ SZYBKI SKAN (Tylko Tętno)")
    print("2. 🌅 RAPORT PORANNY (Sen, Energia, Stres)")
    print("3. 🧪 WYNIKI LABORATORYJNE (Krew, Hormony)")
    print("q. WYJŚCIE")
    
    try:
        wybor = input("\n[WYBÓR] >> ")
        
        if wybor.lower() == 'q': 
            print("Zamykanie systemu...")
            break
        
        # Przygotowanie pustego wiersza danych
        dane = {k: "-" for k in NAGLOWKI}
        
        # Czas automatyczny
        teraz = datetime.now()
        dane["DATA"] = teraz.strftime("%Y-%m-%d")
        dane["GODZINA"] = teraz.strftime("%H:%M:%S")
        godzina = teraz.hour
        
        # Faza dnia
        if 6 <= godzina < 12: faza = "MORNING"
        elif 12 <= godzina < 18: faza = "WORK"
        elif 18 <= godzina < 22: faza = "RECOVERY"
        else: faza = "SLEEP"
        dane["FAZA"] = faza

        # --- LOGIKA TRYBÓW ---
        if wybor == "1": # SZYBKI
            t_str = input(">> Tętno (BPM): ")
            dane["TETNO"] = t_str
            # Szybka analiza Cortexe
            if t_str.isdigit():
                prefix, rada = mozg.analizuj(int(t_str), faza)
                if prefix:
                    print(f"💡 CORTEX: {rada}")
                    interfejs.send_alert(rada)
            dane["STATUS"] = "QUICK_CHECK"

        elif wybor == "2": # PORANNY (Samsung Data)
            print("\n--- ⌚ DANE Z EKRANU ZEGARKA ---")
            dane["TETNO"] = pobierz_input("Tętno spoczynkowe")
            dane["ENERGIA_SCORE"] = pobierz_input("Energy Score (0-100)")
            dane["SEN_H"] = pobierz_input("Długość snu (np. 7.5)")
            dane["STRES_LVL"] = pobierz_input("Poziom stresu (0-100)")
            dane["NASTROJ"] = pobierz_input("Nastrój (1-5)")
            dane["STATUS"] = "MORNING_REPORT"
            
            # Analiza holistyczna
            if dane["ENERGIA_SCORE"] != "-" and dane["ENERGIA_SCORE"].isdigit():
                if int(dane["ENERGIA_SCORE"]) < 50:
                    interfejs.send_alert("Niski poziom energii. Oszczędzaj zasoby.")

        elif wybor == "3": # LAB
            print("\n--- 🩸 WYNIKI BADAŃ (Ręczne) ---")
            dane["LAB_WIT_D3"] = pobierz_input("Witamina D3 (ng/ml)")
            dane["LAB_KORTYZOL"] = pobierz_input("Kortyzol (µg/dL)")
            dane["CUKIER"] = pobierz_input("Glukoza (mg/dL)")
            dane["CISNIENIE"] = pobierz_input("Ciśnienie (np. 120/80)")
            dane["STATUS"] = "LAB_ENTRY"
            print("✅ Zarchiwizowano dane medyczne.")

        else:
            print("Nieznana opcja.")
            continue

        # ZAPIS DO PLIKU
        lista_wartosci = [str(dane[klucz]) for klucz in NAGLOWKI]
        linia = ",".join(lista_wartosci) + "\n"
        
        with open(PLIK_PAMIECI, "a") as plik:
            plik.write(linia)
            print("💾 Zapisano w bazie ULTIMATE.")
            
    except Exception as e:
        print(f"❌ BŁĄD SYSTEMU: {e}")
        time.sleep(1)

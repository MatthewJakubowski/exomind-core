# PLIK: main.py
# SYSTEM EXOMIND v2.0 (Core Logic)

import time
from datetime import datetime
from actuators import BioInterface  # Nerwy
from cortex import Brain            # Mózg Offline (Domyślny)
# from cortex_ai import Brain       # Odkomentuj, by użyć AI

PLIK_PAMIECI = "bio_history.csv"

print("--- 🧬 SYSTEM EXOMIND V2.0 ONLINE 🧬 ---")

# Inicjalizacja modułów
interfejs = BioInterface()
mozg = Brain()

# Inicjalizacja Pamięci
try:
    with open(PLIK_PAMIECI, "x") as f:
        f.write("DATA,GODZINA,FAZA,TETNO,STATUS\n")
except FileExistsError:
    pass 

while True:
    print("\n" + "="*30)
    
    # 1. Zegar Biologiczny
    teraz = datetime.now()
    data_str = teraz.strftime("%Y-%m-%d")
    godz_str = teraz.strftime("%H:%M:%S")
    godzina = teraz.hour
    
    if 6 <= godzina < 12: faza = "MORNING"
    elif 12 <= godzina < 18: faza = "WORK"
    elif 18 <= godzina < 22: faza = "RECOVERY"
    else: faza = "SLEEP"

    print(f"[ZEGAR] {godz_str} | FAZA: {faza}")

    # 2. Input
    try:
        wejscie = input(">> Podaj tętno (lub 'q'): ")
        if wejscie.lower() == 'q': 
            print("Zamykanie systemu...")
            break
        tetno = int(wejscie)
    except ValueError:
        print("❌ Błąd: Wpisz liczbę!")
        continue

    # 3. Analiza (Cortex)
    prefix_statusu, porada = mozg.analizuj(tetno, faza)

    if prefix_statusu:
        print(f"💡 CORTEX: {porada}")
        interfejs.send_alert(porada)
        komunikat = prefix_statusu
    else:
        print("ℹ️ Parametry stabilne.")
        komunikat = "NORMA"

    # 4. Zapis
    with open(PLIK_PAMIECI, "a") as plik:
        linia = f"{data_str},{godz_str},{faza},{tetno},{komunikat}\n"
        plik.write(linia)
        print("💾 Zapisano.")

    time.sleep(1)

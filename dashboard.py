# PLIK: dashboard.py
# WERSJA 2.0: Analityka + Statystyki

import matplotlib.pyplot as plt
import csv
import statistics

PLIK = "bio_history.csv"

print("--- 📊 EXOMIND: RAPORT DZIENNY 📊 ---")

try:
    czasy = []
    tetna = []

    with open(PLIK, "r") as f:
        czytnik = csv.reader(f)
        next(czytnik) # Pomiń nagłówek
        for wiersz in czytnik:
            if len(wiersz) >= 5 and wiersz[3].strip():
                czasy.append(wiersz[1])       # Godzina
                tetna.append(int(wiersz[3]))  # Tętno

    if not tetna:
        print("❌ Brak danych. Uruchom main.py!")
        exit()

    # --- DATA SCIENCE ---
    srednie_tetno = statistics.mean(tetna)
    max_tetno = max(tetna)
    stres_punkty = sum(1 for t in tetna if t > 100)
    stres_procent = (stres_punkty / len(tetna)) * 100

    print(f"\n📈 STATYSTYKI:")
    print(f"-> Pomiary: {len(tetna)}")
    print(f"-> Średnia: {srednie_tetno:.1f} BPM")
    print(f"-> Max:     {max_tetno} BPM")
    print(f"-> Stres:   {stres_procent:.1f}% czasu")
    
    if stres_procent > 50:
        print("\n⚠️ WERDYKT: DZIEŃ KRYTYCZNY.")
    else:
        print("\n✅ WERDYKT: STABILNIE.")

    # --- WYKRES ---
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.plot(czasy, tetna, color='#00ff00', marker='o', label='BPM')
    plt.axhline(y=100, color='red', linestyle='--', label='Granica Stresu')
    plt.fill_between(czasy, 100, tetna, where=[t >= 100 for t in tetna], color='red', alpha=0.3)

    plt.title(f"EXOMIND RAPORT (Avg: {int(srednie_tetno)} BPM)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("❌ Nie znaleziono pliku bio_history.csv")

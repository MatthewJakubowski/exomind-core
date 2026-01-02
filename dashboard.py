# PLIK: dashboard.py
# WERSJA 3.0: Multi-Parametryczna

import matplotlib.pyplot as plt
import csv

PLIK = "bio_history_ultimate.csv" # Nowa baza

print("--- 📊 EXOMIND ULTIMATE RAPORT 📊 ---")

try:
    czasy = []
    tetna = []
    energie = []
    
    with open(PLIK, "r") as f:
        czytnik = csv.reader(f)
        try:
            next(czytnik) # Pomiń nagłówek
        except StopIteration:
            pass

        for wiersz in czytnik:
            # Sprawdzamy czy wiersz ma dane (indeks 3 to tętno, 5 to energia)
            if len(wiersz) > 5:
                # Tętno
                t = wiersz[3]
                e = wiersz[5]
                
                if t.isdigit():
                    czasy.append(wiersz[1][:5]) # Tylko godzina:minuta
                    tetna.append(int(t))
                    
                    # Energia (jeśli wpisana, inaczej 0)
                    if e.isdigit():
                        energie.append(int(e))
                    else:
                        energie.append(None) # Puste miejsce na wykresie

    if not tetna:
        print("❌ Brak danych. Użyj main.py!")
        exit()

    # --- RYSOWANIE (Dwie osie Y) ---
    plt.style.use('dark_background')
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Oś 1: Tętno (Zielona)
    ax1.set_xlabel('Czas')
    ax1.set_ylabel('Tętno (BPM)', color='#00ff00')
    ax1.plot(czasy, tetna, color='#00ff00', marker='o', label='Tętno')
    ax1.tick_params(axis='y', labelcolor='#00ff00')
    ax1.axhline(y=100, color='red', linestyle='--', alpha=0.5)

    # Oś 2: Energia (Żółta) - Rysujemy tylko punkty, gdzie są dane
    if any(energie):
        ax2 = ax1.twinx()
        ax2.set_ylabel('Energy Score (Samsung)', color='yellow')
        # Filtrujemy None, żeby wykres się nie sypał
        valid_indices = [i for i, v in enumerate(energie) if v is not None]
        valid_czasy = [czasy[i] for i in valid_indices]
        valid_energie = [energie[i] for i in valid_indices]
        
        ax2.plot(valid_czasy, valid_energie, color='yellow', marker='s', linestyle=':', label='Energy Score')
        ax2.tick_params(axis='y', labelcolor='yellow')
        ax2.set_ylim(0, 100)

    plt.title("EXOMIND v3.0: Korelacja Stresu i Energii")
    fig.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"❌ Nie znaleziono bazy: {PLIK}")

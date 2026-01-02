# PLIK: dashboard.py
# WERSJA 3.0: Multi-Parametryczna Wizualizacja

import matplotlib.pyplot as plt
import csv

# Czytamy nową bazę danych
PLIK = "bio_history_ultimate.csv"

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
            # Sprawdzamy czy wiersz jest kompletny (ma wystarczająco kolumn)
            if len(wiersz) > 5:
                t = wiersz[3] # Kolumna TETNO
                e = wiersz[5] # Kolumna ENERGIA_SCORE
                
                # Pobieramy tylko wiersze gdzie jest wpisane tętno
                if t.replace('-','').isdigit():
                    czasy.append(wiersz[1][:5]) # Godzina:Minuta
                    tetna.append(int(t))
                    
                    # Czy jest wpisana energia?
                    if e.replace('-','').isdigit():
                        energie.append(int(e))
                    else:
                        energie.append(None) # Puste miejsce na wykresie

    if not tetna:
        print("❌ Brak danych. Uruchom main.py i wybierz opcję 1 lub 2!")
        exit()

    # --- RYSOWANIE WYKRESU (Dual Axis) ---
    plt.style.use('dark_background')
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Oś Lewa: Tętno
    ax1.set_xlabel('Czas')
    ax1.set_ylabel('Tętno (BPM)', color='#00ff00')
    ax1.plot(czasy, tetna, color='#00ff00', marker='o', label='Tętno', linewidth=2)
    ax1.tick_params(axis='y', labelcolor='#00ff00')
    ax1.axhline(y=100, color='red', linestyle='--', alpha=0.5, label='Granica Stresu')

    # Oś Prawa: Energia (Jeśli są dane)
    # Filtrujemy None, żeby narysować tylko istniejące punkty energii
    valid_indices = [i for i, v in enumerate(energie) if v is not None]
    
    if valid_indices:
        ax2 = ax1.twinx()
        ax2.set_ylabel('Energy Score (Samsung)', color='yellow')
        
        valid_czasy = [czasy[i] for i in valid_indices]
        valid_energie = [energie[i] for i in valid_indices]
        
        ax2.plot(valid_czasy, valid_energie, color='yellow', marker='s', linestyle=':', label='Energy Score', markersize=8)
        ax2.tick_params(axis='y', labelcolor='yellow')
        ax2.set_ylim(0, 100)

    plt.title("EXOMIND v3.0: Korelacja Stresu i Energii")
    fig.tight_layout()
    plt.grid(visible=True, alpha=0.1)
    
    print("-> Generowanie wizualizacji...")
    plt.show()

except FileNotFoundError:
    print(f"❌ Nie znaleziono bazy: {PLIK}. Uruchom najpierw main.py!")

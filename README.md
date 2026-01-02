# 🧬 EXOMIND-CORE v2.0 (Biometric Assistant)

ExoMind to osobisty asystent biometryczny napisany w Pythonie (Pydroid 3).
System analizuje tętno i fazę dnia, aby dostarczać porady w czasie rzeczywistym.

## 🏗️ Architektura: Offline First

1.  **Bezpieczeństwo:** Domyślnie używamy lokalnego modułu `cortex.py` (bez chmury).
2.  **Odporność (Fault Tolerance):** System wykrywa brak biblioteki `android-helper` i automatycznie przełącza się w tryb symulacji wirtualnej (tekstowej).

## 📂 Struktura

* `main.py` - Główna logika.
* `actuators.py` - Inteligentny sterownik (Hardware/Virtual).
* `dashboard.py` - Analiza danych i wykresy.
* `cortex.py` - Baza wiedzy (Offline).
* `cortex_ai.py` - Opcjonalny moduł AI (Gemini).

## 🚀 Uruchomienie

1.  Zainstaluj Pydroid 3.
2.  Uruchom `main.py`.

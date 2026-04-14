import requests
import json
import os


# 1. SAJÁT FÜGGVÉNY: Adat lekérése az API-tól
def konyv_adatok_lekerese(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    try:
        valasz = requests.get(url)
        if valasz.status_code == 200:
            adat = valasz.json()
            # Összetett adattípus (szótár) kezelése
            kulcs = f"ISBN:{isbn}"
            if kulcs in adat:
                return adat[kulcs]
        return None
    except Exception as e:
        print(f"Hiba a hívás során: {e}")
        return None


# 2. SAJÁT FÜGGVÉNY: Adatok mentése fájlba (Fájlkezelés)
def mentese_fajlba(konyv_adat, fajlnev="konyvtar.json"):
    konyvtar = []

    # Ha már létezik a fájl, beolvassuk a tartalmát (Összetett adattípus: lista)
    if os.path.exists(fajlnev):
        with open(fajlnev, "r", encoding="utf-8") as f:
            try:
                konyvtar = json.load(f)
            except:
                konyvtar = []

    konyvtar.append(konyv_adat)

    # Írás fájlba
    with open(fajlnev, "w", encoding="utf-8") as f:
        json.dump(konyvtar, f, ensure_ascii=False, indent=4)
    print(f"Sikeresen mentve a(z) {fajlnev} fájlba.")


# 3. SAJÁT FÜGGVÉNY: Formázott megjelenítés
def konyv_kiirasa(konyv):
    cim = konyv.get("title", "Ismeretlen cím")
    szerzok = ", ".join([szerzo['name'] for szerzo in konyv.get("authors", [])])
    ev = konyv.get("publish_date", "Nincs adat")
    print(f"\n--- Könyv adatai ---\nCím: {cim}\nSzerző(k): {szerzok}\nKiadás éve: {ev}\n--------------------")


# FŐPROGRAM (Vezérlési szerkezetek)
def main():
    print("Üdvözöllek a Könyvkeresőben!")
    while True:
        isbn = input("\nAdj meg egy ISBN számot (vagy 'exit' a kilépéshez): ")

        if isbn.lower() in ["exit", "quit"]:
            break

        # Minimális validáció (Feltétel)
        if len(isbn) < 10:
            print("Ez nem tűnik érvényes ISBN számnak.")
            continue

        adat = konyv_adatok_lekerese(isbn)

        if adat:
            konyv_kiirasa(adat)
            mentese_fajlba(adat)
        else:
            print("Sajnos nem találtam ilyen könyvet.")


if __name__ == "__main__":
    main()
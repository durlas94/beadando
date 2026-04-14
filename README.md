# Könyvkereső és Digitális Könyvtár

Ez a program a féléves kötelező feladatomra készült. Segítségével ISBN szám alapján kereshetünk könyveket az interneten, és elmenthetjük őket egy saját listába.

## Választott téma
1. Könyvkereső program az Open Library API használatával.

## Funkciók
* **Keresés:** Az Open Library API-n keresztül lekéri a könyv címét, szerzőjét és kiadási évét.
* **Mentés:** A lekérdezett adatokat automatikusan elmenti egy `konyvtar.json` fájlba.
* **Visszatöltés:** Ha újraindítjuk a programot, a korábbi mentéseink megmaradnak.

## Felhasznált technológiák (Követelmények teljesítése)
* **Fájlkezelés:** `json` fájlok írása és olvasása.
* **HTTP hívás:** `requests` modul használata külső API eléréséhez.
* **Összetett adattípusok:** Listák és szótárak (dictionaries) használata.
* **Saját függvények:** 3 különálló függvény a moduláris felépítésért.

## Hogyan futtasd?
1. Telepítsd a szükséges kiegészítőt:
   ```bash
   pip install requests

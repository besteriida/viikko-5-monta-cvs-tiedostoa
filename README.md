# viikko-5-monta-cvs-tiedostoa
Tehtävänäsi on laatia Python-ohjelma, joka:

Lukee tiedot tiedostoista viikko41.csv, viikko42.csv ja viikko43.csv

Laskee jokaiselle viikonpäivälle (ma–su) samankaltaisen yhteenvedon kuin tehtävässä A:

vaiheittaisen sähkönkulutuksen (vaihe 1–3) kWh-yksikössä
vaiheittaisen sähköntuotannon (vaihe 1–3) kWh-yksikössä
Tallentaa kaikki yhteenvedot tiedostoon yhteenveto.txt selkeänä, käyttäjäystävällisenä raporttina (ei pelkkää raakadataa).

Tiedostot sisältävät viikkojen 41, 42 ja 43 tuntikohtaiset mittaukset:

aika (päivämäärä ja kellonaika)
kulutus kolmeen vaiheeseen jaettuna (Wh)
tuotanto kolmeen vaiheeseen jaettuna (Wh)
Sinun tehtäväsi on muuntaa Wh → kWh ja esittää tulokset kahden desimaalin tarkkuudella, käyttäen pilkkua desimaalierottimena raportissa.

Note

Halutessa työn voi tehdä pareittain (max. kaksi). Tällöin kohdassa Palautusohje Itslearningiin pari tekee vain yhden palautuksen, johon on yhdistetty molemmat.

⚖️ Yksikkö: Wh → kWh
Tiedostoissa arvot ovat Wh. Raportissa (yhteenveto.txt) kaikki energia-arvot tulee esittää kWh-yksikössä.

1️⃣ Ohjelman toiminnallisuus
Ohjelman tulee:

Lukea kaikki kolme CSV-tiedostoa: viikko41.csv, viikko42.csv, viikko43.csv.

Laskea jokaiselle viikolle (41, 42, 43) päiväkohtaiset summat:

viikonpäivä suomeksi (maanantai, tiistai, …)
päivän päivämäärä muodossa pv.kk.vuosi (esim. 13.10.2025)
kulutus vaiheittain 1–3 (kWh, 2 desimaalia, pilkku desimaalina)
tuotanto vaiheittain 1–3 (kWh, 2 desimaalia, pilkku desimaalina)
Kirjoittaa yhteenvedot tiedostoon yhteenveto.txt seuraavalla ajatuksella:

Raportissa on selkeä otsikko jokaiselle viikolle, esim.:
Viikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)
Päivä        Pvm         Kulutus [kWh]              Tuotanto [kWh]
                         v1      v2      v3         v1      v2      v3
---------------------------------------------------------------------------
maanantai    06.10.2025  12,35   1,56    2,78       0,01   0,39    0,52
tiistai      07.10.2025  ...
...
sunnuntai    12.10.2025  ...
Sama rakenne viikoille 42 ja 43 saman raportin sisällä.

Ohjelma pitää rakentaa funktioiden varaan, ei ”kaikki koodi suoraan tiedoston juureen”.

Käytä funktiota, esim.:
def lue_data(tiedoston_nimi: str) -> list:
    """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa."""
    ...
Funktiota, joka laskee päiväkohtaiset yhteenvedot yhdelle viikolle.

Funktiota, joka muodostaa rivit raporttia varten (merkkijonoiksi).

Funktiota, joka kirjoittaa raportin tiedostoon yhteenveto.txt.

Tee myös pääfunktio, esimerkiksi:

def main() -> None:
    """Ohjelman pääfunktio: lukee datan, laskee viikkoyhteenvedot ja kirjoittaa raportin tiedostoon."""
    ...

    Ohjelmassa tulee käyttää ainakin:

Muuttujia (esim. päiväkohtaiset summat, viikkotasoiset summat)

Listoja tai muita tietorakenteita (esim. listat viikon päivistä)

Toistorakennetta (for) rivien ja päivien läpikäyntiin

Ehtolauseita (if) – erityisesti:

päivien ryhmittelyyn / valintaan
mahdollisesti ”parhaan / huonoimman” päivän valintaan
Funktioita, joissa on:

docstring
tietotyyppivihjeet
Lisäksi tarvitaan:

Tiedoston kirjoittamista (open("yhteenveto.txt", "w", encoding="utf-8")) käyttäen with-rakennetta, jotta tiedosto sulkeutuu varmasti oikein.


Myöhempää tarkastelua varten, jos tekee näin pitää tehä looppi eli avaa mieluummin pandan avulla. Nyt rakennan tällä import tavalla koska harjoittelen sitä eli älä lunttaa tästä kun oot kehittynyt: 

import csv

from datetime import datetime

def lue_csv_tiedosto(filename: str) -> list:
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        header = next(reader)  # ohitan otsikkorivin




import csv
import glob

from datetime import datetime
import re

def read_first_two_lines(path: Path) -> tuple[str, str]:
    with open(path, "r", encoding="utf-8-sig") as f:
        first = f.readline().rstrip("\n")
        second = f.readline().rstrip("\n")
    return first, second


def lue_kaikki_rivit() -> list:
    kaikki_rivit = []

    for filename in glob.glob("*.csv"): # jokerikortti joka etsii kaikki tiedostot jotka päättyy .csv
        match = re.search(r'viikko(\d+)\.csv', filename)
        if match:
            viikkonumero = match.group(1)
            print(f"Viikko {viikkonumero}: käsitellään {filename}")
        else:
             print(f"Tiedostoa {filename} ei käsitellä, koska se on nimetty väärin (lisää viikkonumero).")
             continue

        with open(filename, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            header = next(reader, None)  # lue ensimmäinen rivi otsikoksi
            if header is None:
                print(f"Tiedosto {filename} ei sisällä otsikkoa, ohitetaan.")
                continue

            print("Otsikko:", header)  # debug
            for row in reader:
                if not row or not row[0].strip():
                    continue
                aika = datetime.strptime(row[0].strip(), '%Y-%m-%dT%H:%M:%S')
                kaikki_rivit.append({
                    "viikko": int(viikkonumero),
                    "aika": aika,
                    "kulutus1": float(row[1]) / 1000,
                    "kulutus2": float(row[2]) / 1000,
                    "kulutus3": float(row[3]) / 1000,
                    "tuotanto1": float(row[4]) / 1000,
                    "tuotanto2": float(row[5]) / 1000,
                    "tuotanto3": float(row[6]) / 1000,
                })

    return kaikki_rivit

def laske_viikot (kaikki_rivit: list) -> dict:
    fi_days = ['Maanantai', 'Tiistai', 'Keskiviikko',
               'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai']
    # suomenkieliset viikonpäivät koska python puhuu englantia
    data = {}    
    
    for rivi in kaikki_rivit:
        viikko = int(rivi["viikko"])     
        # käydään rivit läpi
        viikonpaiva = fi_days[rivi["aika"].weekday()]
        # määritetään viikonpäivä suomeksi

        if viikko not in data:
            data[viikko] = {day: {
                "kulutus": [0, 0, 0],
                "tuotanto": [0, 0, 0],
                "paivamaara": None,
                "viikkonumero": viikko                
            } for day in fi_days}

        if data[viikko][viikonpaiva]["paivamaara"] is None:
            # jos päivämäärä on tyhjä niin asetetaan se
            data[viikko][viikonpaiva]["paivamaara"] = rivi["aika"].date()
            # asetetaan päivämäärä ja viikonpäivä
        data[viikko][viikonpaiva]["viikkonumero"] = viikko

        for i in range(3):
            # käydään kolme arvoa läpi muuttujan nimeltä i avulla ja lisätään ne kulutus ja tuotanto alle
            data[viikko][viikonpaiva]["kulutus"][i] += rivi[f"kulutus{i+1}"]
            data[viikko][viikonpaiva]["tuotanto"][i] += rivi[f"tuotanto{i+1}"]
        
    print("Viikot datassa:", sorted(data.keys()))
    return data

def tulosta_tulokset(data: dict):
     for viikkonumero in sorted(data.keys()):
        viikon_data = data[viikkonumero]
        print(f"\nViikon {viikkonumero} sähkönkulutus ja -tuotanto (kWh, vaiheittain):")
        print(f"📅 {'Päivä':<12} | {'Pvm':<10} | "
              f"{'K1':>6} | {'K2':>6} | {'K3':>6} | "
              f"{'T1':>6} | {'T2':>6} | {'T3':>6}")
        print("-" * 96)
       

        for day, arvot in viikon_data.items():
            k = arvot["kulutus"]
            t = arvot["tuotanto"]
            p = arvot["paivamaara"]
            p_str = p.strftime('%d.%m.%Y') if p else "-"
            print(f"|💡🪫 {day:<12} | {p_str:<10} | "
                  f"{f'{k[0]:.2f}'.replace('.', ','):>8} | "
                  f"{f'{k[1]:.2f}'.replace('.', ','):>8} | "
                  f"{f'{k[2]:.2f}'.replace('.', ','):>8} | "
                  f"{f'{t[0]:.2f}'.replace('.', ','):>8} | "
                  f"{f'{t[1]:.2f}'.replace('.', ','):>8} | "
                  f"{f'{t[2]:.2f}'.replace('.', ','):>8}")


def main():
    kaikki_rivit = lue_kaikki_rivit()
    data = laske_viikot(kaikki_rivit)
    tulosta_tulokset(data)

if __name__ == "__main__":
    main()


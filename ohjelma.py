from datetime import datetime, date

def muunna_tiedot(tietue: list) -> list:
    return [
        datetime.fromisoformat(tietue[0]),
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
    ]
    """ Aloin rakentaan tätä mun viime viikon koodin päälle, ja en saanut sitä MITENKÄÄn toimimaan. Muokkasin sitä niin paljon, että mun oli pakko poistaa kaikki ja aloittaa ihan alusta. Mä en tiedä, oliko ongelma se, että mun viime viikon toteutuksen def lue_data(filename: str) -> list:
    lukee csv-tiedoston missä stringejä ja palauttaa listan. Koska sit kun vaihto ton list -> list niin alko toimimaan. Toi str -> list palautti aina vaan sen ekan viikon, ja ei tunnistanut mitenkään noista kahdesta muusta otsikkoriviä, ja sit alko meneen niin psykoks copilotin ohjeet sen kiertämiseksi että en halunnut käyttää. Copilot tarjosi sitä panda toteutusta, mutta en halunnut koittaa kun en osaa vielä. 
    rivit = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        # avaa tiedoston ja asettaa ton utf merkistön
        reader = csv.reader(csvfile, delimiter=';')
        # määrittää että erotinmerkki eli tietojen välissä on puolipiste
        header = next(reader)
        # ohitetaan otsikkorivi jossa kerrotaan mitä noi tiedot on
    Tässä kuitenkin nyt toimiva versio, jos keksit mikä vikana tossa mun 5A osassa niin kuulen mielelläni. Tässä siis nyt otetaan lista ja luetaan se listana ja asetetaan tiedoille arvot.
    """


def lue_data(tiedoston_nimi: str) -> list:
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for rivi in f:
            tietue = rivi.strip().split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta
    """
    Tässä luetaan yksittäinen tiedosto, ohitetaan otsikkorivi ja kutsutaan muunna_tiedot funktiota joka muuttaa stringit oikean tyyppisiksi arvoiksi.
    Käsitellään myös merkistö utf-8:na ja luetaan rivit splitillä välimerkki ;:stä.
    """


def lue_useat_tiedostot(tiedostot: list) -> list:
    tietokanta = []
    for tiedosto in tiedostot:
        tietokanta.extend(lue_data(tiedosto))
    return tietokanta
    """
    Tämä funktio lukee useita tiedostoja ja yhdistää niiden tiedot yhdeksi isoksi tietokannaksi kutsumalla lue_data funktiota jokaiselle tiedostolle. 
    """


def paivantiedot(paiva: date, tietokanta: list) -> list:
    kulutus = [0, 0, 0]
    tuotanto = [0, 0 ,0]
    for tietue in tietokanta:
        if tietue[0].date() == paiva:
            kulutus[0] += tietue[1] /1000
            kulutus[1] += tietue[2] /1000
            kulutus[2] += tietue[3] /1000
            tuotanto[0] += tietue[4] /1000
            tuotanto[1] += tietue[5] /1000
            tuotanto[2] += tietue[6] /1000

    return [
        f"{paiva.day}.{paiva.month}.{paiva.year}",
        f"{kulutus[0]:.2f}".replace('.', ','),
        f"{kulutus[1]:.2f}".replace('.', ','),
        f"{kulutus[2]:.2f}".replace('.', ','),
        f"{tuotanto[0]:.2f}".replace('.', ','),
        f"{tuotanto[1]:.2f}".replace('.', ','),
        f"{tuotanto[2]:.2f}".replace('.', ','),
    ]
    """
    Tässä muutetaan annetun päivän tiedot yhdeksi riviksi, jossa on kulutus ja tuotanto kWh:na kolmessa vaiheessa pilkulla käyttäjäystävällisesti eroteltuna.
    """


def main():
    import glob
    tiedostot = glob.glob("*.csv")   # kaikki csv:t hakemistosta

    for tiedosto in tiedostot:
        kulutusTuotantoDB = lue_data(tiedosto)

        viikko = tiedosto.replace(".csv", "").replace("viikko", "")
        otsikko = f"🎄⛄🎅 Viikon {viikko} sähkön kulutus ja tuotanto vaiheittain kWh"

        print("\n" + otsikko + "\n")
        print("Päivät\t\tPvm\t\tKulutus kWh")
        print("\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
        print("-" * 90)

        paivat = sorted({tietue[0].date() for tietue in kulutusTuotantoDB})
        for paiva in paivat:
            viikonpaiva_suomeksi = {
                "Monday": "maanantai",
                "Tuesday": "tiistai",
                "Wednesday": "keskiviikko",
                "Thursday": "torstai",
                "Friday": "perjantai",
                "Saturday": "lauantai",
                "Sunday": "sunnuntai",
            }[paiva.strftime("%A")]

            # Muotoillaan sarakkeet: viikonpäivä 12 merkkiä leveä, pvm 12 merkkiä leveä
            paiva_str = f"{paiva.day:02}.{paiva.month:02}.{paiva.year}"
            tiedot = paivantiedot(paiva, kulutusTuotantoDB)[1:]  # ohitetaan pvm, koska tulostetaan erikseen ja kun en ohittanut rivittyi typerän näköisesti

            print(f"{viikonpaiva_suomeksi:<12}{paiva_str:<12}" + "\t".join(tiedot))
    """
    Tässä muutetaan tiedoston nimi tulostukseen johon jää vaan viikkonumero eli poistetaan se sana viikko ja .csv pääte.
    Sitten muotoillaan haluttu otsikkotulostus ja käydään päivät läpi kutsuen paivantiedot funktiota. Sit tulostetaan se rivi ja välissä on tabulaattorit. Määritellään myös viikonpäivät suomeksi.
    Sitten tuli muuten hyvä tulostus, mutta oli rivit tyhmän pomppivia niin lisäsin vielä tonne noi sarakkeiden muotoilut ja otin veks pvm kun muuten tuli sekava printtaus.
    """


if __name__ == "__main__":
    main()
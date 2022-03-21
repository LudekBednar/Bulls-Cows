import random

def uvod():
    """Funkce vypise uvodni hlavicku."""
    oddelovac = 50 * "-"
    print("Ahoj!")
    print(oddelovac)
    print("""Vygeneroval jsem pro vás náhodné čtyřmístné číslo.
Pojďme si zahrát hru bulls and cows.""")
    print(oddelovac)


def generator_cisla():
    """Funkce generuje nahodne cislo dle pozadavku zadani. Vraci jeho hodnotu."""
    cislo = []
    seznam_cisel_1 = list(range(10))
    # seznam_cisel_2 zajisti, ze na prvni cifre nebude nula (vybira se z intervalu 1 az 9).
    seznam_cisel_2 = list(range(1, 10))
    for i in range(4):
        cifra = random.choice(seznam_cisel_2)
        seznam_cisel_1.remove(cifra)
    # pote co se vybere prvni cifra, tak dalsi cifry jiz mohou obsahovat nulu proto seznam_cisel_2 = seznam_cisel_1.
        seznam_cisel_2 = seznam_cisel_1
        cislo.append(str(cifra))
    return "".join(cislo)


def vstup():
    """Funkce si vyzada vstupni cislo od uzivatele a zkontroluje spravnost jeho zadani.
    Pokud je vse spravne zadane, vrati hodnotu zadnanou uzivatelem."""

    # podminka bude True dokud nezadame spravne cislo.
    podminka = True
    while podminka:
        # Nyni se zjistuje, zdali cislo neobsahuje vice stejnych cifer.
        # podminka vyskyt_vice_cifer bude "True" pokud se cifry v zadani cisla opakuji.
        vyskyt_vice_cifer = False
        tip = input("Zadej cislo: ")
        vyskyt_cifer = {}
        for i in tip:
            vyskyt_cifer[i] = vyskyt_cifer.get(i, 0) + 1
        for i in vyskyt_cifer:
            if vyskyt_cifer[i] != 1:
                vyskyt_vice_cifer = True

        if vyskyt_vice_cifer:
            print("Cifry se opakují, zadej 4 unikátní cifry.")

        if len(tip) != 4:
            print("Zadal jsi špatný počet cifer, zadej číslo obsahující přesně 4 cifry.")

        if tip[0] == "0":
            print("Číslo nesmí začínat nulou.")

        if tip.isdigit() == False:
            print("Zadal jsi nečíslenou hodnout, zadej číslo.")

        # Pokud je vse zadane spravne, while cyklus se ukonci. Vrati se hodnota zadana uzivatelem.
        if vyskyt_vice_cifer == False and len(tip) == 4 and tip[0] != "0" and tip.isdigit() == True:
            podminka = False
            return tip


def vypis_byci(pocet_byku):
    """Funkce zajisti spravny vypis jednotneho a mnozneho cisla (bull / bulls)."""
    if pocet_byku in (0, 2, 3):
        return "bulls"
    else:
        return "bull"

def vypis_kravy(pocet_krav):
    """Funkce zajisti spravny vypis jednotneho a mnozneho cisla (cow / cows)."""
    if pocet_krav in (0, 2, 3):
        return "cows"
    else:
        return "cow"

def hodnoceni(pocet_kol):
    """Funce vypise slovni hodnoceni dle dosazeneho poctu tipu. """
    if pocet_kol in tuple(range(1, 4)):
         print("Neskutečný výsledek!")
    if pocet_kol in tuple(range(4, 10)):
        print("Dobrý výsledek!")
    if pocet_kol in tuple(range(10, 21)):
        print("Mohlo to být lepší.")
    if pocet_kol > 20:
        print("Moje kočka by to zvládla lépe.")

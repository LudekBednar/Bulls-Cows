from Pomocnefunkce import *


def hlavni(zadani, tip_pc):
    """V hlavni funkci probiha hodnoceni tipu zadaneho uzivatelem (funkce vstup())
    a cisla vygenerovaneho pocitacem (funkce generator_cisla())"""

    pocet_krav = 0
    pocet_byku = 0
    pocet_kol = 0
    podm = True
    # podm zajistuje, ze cyklus bezi dokud uzivatel neuhodne cislo.
    while podm:
        print(50 * "-")
        for i in range(4):
            if zadani[i] == tip_pc[i]:
                pocet_byku += 1
            if zadani[i] != tip_pc[i] and zadani[i] in tip_pc:
                pocet_krav += 1
        if zadani == tip_pc:
            podm = False
            pocet_kol += 1
            print("Správně, uhodl jsi číslo ve", pocet_kol, "tipech.")
        else:
            print(zadani)
            print(pocet_byku, vypis_byci(pocet_byku), ",", pocet_krav, vypis_kravy(pocet_krav))
            print(50 * "-")
            zadani = vstup()
            pocet_byku = 0
            pocet_krav = 0
            pocet_kol += 1
    hodnoceni(pocet_kol)


if __name__ == "__main__":
    uvod()
    hlavni(vstup(), generator_cisla())

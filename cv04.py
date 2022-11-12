# funkce
"""
v C/C++/C#/...
datovy_typ jmeno_funkce(typ parameter1, ...)
{
    nějaká činnost
}
"""
def pozdrav_me(jmeno: str ):    #vyžadujeme typ parametru "str"
    jmeno = str(jmeno)  # ať zadáte cokoliv, převedu to na text
    print("Čauko " + jmeno)
    print("Čauko {}".format(jmeno))
    print(f"Čauko {jmeno}") #tzv. f-String

    return "OK"

def pozdrav_me_2(jmeno, vek=18, dzender="racek"):
    print(f"Ahoj {jmeno}, našel jsem, že ti je {vek} a jsi {dzender}")
    print("Ahoj {0}, našel jsem, že"
          " ti je {1} a jsi {2}".format(jmeno, vek, dzender))
    print(f"Ahoj " + jmeno + ", našel jsem, že ti"
                             " je "+str(vek)+" a jsi "+dzender)

    return -69

pozdrav_me("Juraj")
pozdrav_me(1)
pozdrav_me_2("Tomáš", 20, "ne-člověk")
pozdrav_me_2("Kryštof Samuel")
pozdrav_me_2("Ing. M@t3$",
             dzender="vykolejovač rychlíků",
             vek=19)

"""
zkuste vytvořit funkci "kalkulačka":
- přijme dvojici čísel
- budete si moci vybrat operaci (+,-,*,/,^)
- vypíšete hezky výsledek
- výsledek vrátíte
- základní operace bude sčítání
"""
# vstup z klávesnice pomocí funkce input() - VŽDY vrací string
# int(), float() - převedeme string na číslo
vstup_1 = float(input("Zadej prosím první číslo: "))
vstup_2 = float(input("Zadej prosím druhé číslo: "))
vstup_3 = input("Zadej prosím operaci čísel: ")

def kalkulacka(cislo_1: float, cislo_2: float, operace):
    # by Samíq
    if(operace == "+"):
        vysledek = cislo_1 + cislo_2
    elif(operace == "-"):
        vysledek = cislo_1 - cislo_2
    elif (operace == "*"):
        vysledek = cislo_1 * cislo_2
    elif (operace == "/"):
        vysledek = cislo_1 / cislo_2
    else:
        print("Tahle operace není dovolena")
        return "Tahle operace není dovolena"

    print(f"{cislo_1} {operace} {cislo_2} = {vysledek}")

    return vysledek

kalkulacka(vstup_1, vstup_2, vstup_3)
#ahoj ^^)/
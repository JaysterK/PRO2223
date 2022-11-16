def readB(x):
 with open(r'C:/Git/PRO2223/PRO2223/texty/wiki.txt',encoding="utf8") as soubor:
    for int, line in enumerate(soubor):
            if x in line:
             print('Text obsahuje zakázané slovo', x)
             print('Číslo řádku:', int)
             print('Řádek:', line)
             break

def readA():
 with open(r'C:/Git/PRO2223/PRO2223/texty/slova.txt', encoding="utf8") as slova:
    for line in slova:
        readB(line)

readA()
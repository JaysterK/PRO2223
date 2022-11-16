kontolni_text = []
with open("texty/wiki.txt", "r", encoding="UTF-8") as soubor:
    kontolni_text = soubor.readlines()

kontolni_text = "".join(kontolni_text)

kontolni_text =kontolni_text.split("\n")

k_cenzure = []
with open("texty/slova.txt", "r", encoding="UTF-8") as soubor:
    k_cenzure = soubor.readlines()

k_cenzure = "".join(k_cenzure)
k_cenzure =k_cenzure.split("\n")

zavadne = False
i_radek = 0
for radek in kontolni_text:
    i_radek +=1
    for slovo in k_cenzure:
        if slovo in radek:
            print(f"nalezene slovo '{slovo}' na řádku {i_radek} ")
            zavadne = True
            break
    if zavadne:
        break

if not zavadne:
    print("Text je publikovatelný ve stranický noviných")


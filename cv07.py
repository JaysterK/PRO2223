"""
Zkusíme si práci s textem a soubory
"""
# starší
soubor = open("texty/text_1.txt", "r", encoding="utf-8")
obsah_souboru = soubor.readlines()
soubor.close()

# novější
with open("texty/text_1.txt", "r", encoding="utf-8") as soubor:
    obsah_souboru = soubor.readlines()

print(obsah_souboru)


# spojování stringů, které jsou uloženy v poli
text = "".join(obsah_souboru)
print(text)

# provedeme nahrazení "ošklivých" znaků ničím/mezerou
text = text.replace("\n", " ")
text = text.replace(",", "")
text = text.replace("-", "")
text = text.replace(".", "")
text = text.replace("(", "")
text = text.replace(")", "")

# rozdělení textu, kde vybraný znak (sérii znaků) nahradíte mezerou
text_slova = text.split(" ")

print(text_slova)

"""
Jakkoliv najděte nejčastěji se vyskytující slovo --> POZOR, není to mezera
"""
# od MG
from collections import Counter
Counter = Counter(text_slova)
most_occur = Counter.most_common(10)
print("Nejčastější slovo v textu je: ", most_occur)

# ručně
cetnost_slov = {}   # slovník
# projdu všechna slova, jedno po druhém
for slovo in text_slova:
    # co se mi nelíbí, to přeskočím
    if slovo == "":
        continue
    # už jsem to slovo někdy četl?
    if slovo in cetnost_slov.keys():
        cetnost_slov[slovo] += 1    # zvýším četnost o 1
    else:
        cetnost_slov[slovo] = 1  # je to první výskyt

print(cetnost_slov)
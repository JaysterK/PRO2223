# hraní si se slovníkem
slovnik = {
    "uzivatelske_jmeno": "M@t3$",
    "heslo":"M@t3$321",
    "vek":20,
    "povolani":"syn",
    "pohlavi":True,
    "otrokar":True,
    "kamaradi":["Kouba", "Kuba"]
}
print(slovnik["heslo"])
print(slovnik.keys())
print(slovnik.values())
print("auto" in slovnik.keys()) # vrátí True/False je-li klíč přítomen
print(slovnik)

if "auto" in slovnik.keys():
    print(slovnik["auto"])
else:
    print("Nie je")
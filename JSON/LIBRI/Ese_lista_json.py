import json

with open("JSON/LIBRI/libri.json", "r") as file:
    libri = json.load(file)

print(libri)


for libro in libri:
    libro_da_trovare = "Il Signore degli Anelli"
    if libro["titolo"] == libro_da_trovare:
        print(f"libro trovato {libro['titolo']} di {libro['autore']}")
    else:
        print(f"libro non trovato: {libro_da_trovare} ")
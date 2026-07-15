import json

# caricamento in dizionario del file obj_json -> dict
with open("JSON/persona.json", "r") as file:
    dati = json.load(file)
print(dati)


# MODIFICHIAMO UNA VAR 
dati["eta"] = dati["eta"] + 1
print(dati)


# SCRIVIAMO IL FILE CON LA NUOVA VAR

with open("JSON/persona.json", "w") as file:
    json.dump(dati, file, indent=4)     #json.dump trasforma da dict -> json_obj


# Dizionari stamparli e selezionare

persona = {
    "nome": "Michele",
    "cognome": "Rucci",
    "age": 22,
}

print(persona)
print(f"nome persona {persona['nome']}")

trova_age = 22

if persona["age"] == trova_age:
    print(f"della persona {persona} e' stata trovata l'age di {trova_age}")
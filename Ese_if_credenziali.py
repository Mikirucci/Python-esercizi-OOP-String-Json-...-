#CONTROLLI SEMPLICI TRA VARIABILI 

def login(nome, password):
    
    if nome == "admin" and password == "admin123":
        accesso  = True
        print(f"accesso come {nome} CORRETTO")
        return accesso
    else:
        print(f"accesso come {nome} NEGATO")
        accesso = False
    return accesso

user = input("inserici username ")
password = input("inserisci password ")

log = login(user, password)
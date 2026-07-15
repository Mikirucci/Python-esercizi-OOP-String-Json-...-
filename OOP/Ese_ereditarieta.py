
class Persona:
    
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    # def to_string(self):
    #     print(f"PERSONA - nome: {self.nome}, cognome: {self.cognome}")
    def __str__(self):
        return f"nome: {self.nome}, cognome: {self.cognome}"
    
    
# STUDENTE - aggiungiamo - Matricola   
class Studente(Persona):
    
    def __init__(self, nome, cognome, matricola):
        super().__init__(nome, cognome)
        self.matricola = matricola
        
    # def to_string(self):
    #     print(f"STUDENTE - {self.nome} {self.cognome} - Matricola: {self.matricola}")
    def __str__(self):
        return f"nome: {self.nome}, cognome: {self.cognome}, matricola: {self.matricola}"
    
    
# PROFESSORE - aggiungiamo - Materia
        
class Professore(Persona):
    
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia
    
    # def to_string(self):
    #     print(f"PROFESSORE - {self.nome} {self.cognome} - Materia: {self.materia}")
    def __str__(self):
        return f"nome: {self.nome}, cognome: {self.cognome}, materia: {self.materia}"
    
    
    
# COSTRUZIONE DEGLI OGGETTI
persona = Persona("Michele", "Rucci") 
studente = Studente("Michele", "Rucci", 1234)       # CONCATENARE CON .to_string() PER STAMPARE TUTTI I DATI
professore = Professore("Michele", "Rucci", "matematica")


# MODO PER STAMPARE TUTTI GLI OGGETTI IN MODO UNICO IN UNA LISTA
persone = [persona, studente, professore]
for p in persone:
    print(p)   # stampa l'oggetto persona, studente e professore in modo leggibile grazie al metodo __str__ definito in ciascuna classe
    
    
# non si usa to_string in python ma si usa def __str__ per stampare l'oggetto in modo leggibile
# per esempio def __str__(self): return f"nome: {self.nome}, cognome: {self.cognome}, eta: {self.eta}"
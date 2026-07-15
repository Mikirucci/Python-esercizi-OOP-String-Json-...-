# per rappresentare la classe astratta in python si usa il modulo abc (Abstract Base Class)

from abc import ABC, abstractmethod

class Persona(ABC):
    
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
      
    # abbiamo definito un metodo astratto che deve essere implementato in tutte le classi figlie  
    @abstractmethod
    def to_string(self):
        pass
    
    @abstractmethod
    def test_function(self):
        pass
    

class Studente(Persona):
    
    def __init__(self, nome, cognome, matricola):
        super().__init__(nome, cognome)
        self.matricola = matricola
        
    def to_string(self):   
        print(f"STUDENTE - {self.nome} {self.cognome} - Matricola: {self.matricola}")
    
    def test_function(self):
        print("sono uno studente")
        
class Professore(Persona):
    
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia
    
    def to_string(self):
        print(f"PROFESSORE - {self.nome} {self.cognome} - Materia: {self.materia}")
        
    def test_function(self):
        print("sono un professore")
        

studente = Studente("Michele", "Rucci", 1234)  
professore = Professore("Domenico", "Rucci", "matematica")

# salviamo in lista e printiamo tutti gli oggetti in modo leggibile grazie al metodo to_string() definito in ciascuna classe
persone = [studente, professore]
for p in persone:
    p.to_string()  
    p.test_function()
    print(" ")





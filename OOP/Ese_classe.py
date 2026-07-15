# CLASSE CHE RAPPRESENTA UNA PERSONA

class persona:
    
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        
    def to_string(self):
        print(f"nome: {self.nome}, cognome: {self.cognome}, eta: {self.eta}")
        
    
persona_n1 = persona("Michele", "Rucci", 22)

persona_n1.to_string()
        
        
        
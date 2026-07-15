
class ContoBancario:
    
    def __init__(self, nome, cognome, saldo):
        self.nome = nome
        self.cognome = cognome
        self.saldo = saldo
        
    def mostra_saldo(self):
        print(f"il tuo saldo attuale e' di {self.saldo}")     
    
    def versamento(self, importo_versato):
        self.saldo += importo_versato
        print(f"versamento di {importo_versato} euro effettuato, nuovo saldo: {self.saldo}")
    
    def prelievo(self, importo_prelevato):
        if importo_prelevato > self.saldo:
            print(f"saldo non sufficuente per il prelievo di {importo_prelevato} - saldo: {self.saldo}")   
        else:
            self.saldo -= importo_prelevato
            print(f"prelivo SUCCESS di {importo_prelevato}, saldo rimanente: {self.saldo}")
            
    
conto_bancario = ContoBancario("Michele", "Rucci", 1000)


while True: # quando l'utente inserisce 0 il programma esce dal ciclo while e termina perche diventa FALSE
    try:
        scelta_utente = int(input("scegli operazione: 1 - mostra saldo, 2 - versamento, 3 - prelievo, 0 - esci: "))
        match scelta_utente:
            case 1:
                conto_bancario.mostra_saldo()
            case 2:
                versamento = int(input("inserisci importo da versare: "))
                conto_bancario.versamento(versamento)
            case 3:
                prelievo = int(input("inserisci importo da prelevare: "))
                conto_bancario.prelievo(prelievo)
            case 0:
                print("uscita dal programma")
                break
            
    except ValueError:  # per eccezione generica Exception as e: print(f"errore generico {e}")  
        print("inserisci un numero valido")
    










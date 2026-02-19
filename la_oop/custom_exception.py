# La classe che definisce l'eccezione personalizzata
# deve ereditare dalla classe Exception.
class EmailNonValida(Exception):
    def __init__(self, email, messaggio = "Email non valida!"):
        self.email = email
        self.messaggio = messaggio
        super().__init__(f"{messaggio}:{email}")

def verifica_email(email):
    while email:
        if "@" not in email:
            raise EmailNonValida(email)

try:
    email = input("Inserisci una email")
    verifica_email(email)
except EmailNonValida as e:
    print(e)




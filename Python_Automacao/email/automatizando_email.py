from imbox import Imbox
import json

with open("credenciais_gmail.json", "r") as file:
    credenciais = json.loads(file.read())

email = credenciais["email"]
senha = credenciais["password"]
servidor = credenciais["host"]

with Imbox(hostname=servidor,
           username=email,
           password=senha) as imb:

    mensagens = imb.messages(unread=True)

    if not mensagens:
        print("Erro ao acessar!")
    else:
         print("Acesso Ok!")

    print(f"Mensagens não lidas: {len(mensagens)}")

    for uid, msg in mensagens:
        print(f"De: {msg.sent_from[0]['email']}")
        print(f"Assunto: {msg.subject}")
        print("\n")

from imbox import Imbox
import json
from datetime import date

with open("credenciais_gmail.json", "r") as file:
    credenciais = json.loads(file.read())

email = credenciais["email"]
senha = credenciais["password"]
servidor = credenciais["host"]

with Imbox(hostname=servidor,
           username=email,
           password=senha) as imb:

    # filtrando por mensagens não lidas
    # mensagens = imb.messages(unread=True)

    # filtrando pelo email que envia:
    # mensagens = imb.messages(sent_from= "contato@datascienceacademy.com.br")

    # filtrando pelos emails enviados:
    # mensagens = imb.messages(sent_to= "neuron.datagirls@gmail.com")

    # filtrando por datas:
    # mensagens = imb.messages(date__on = date(2026, 5, 15))

    # filtrando por datas: após a data informada
    # mensagens = imb.messages(date__gt = date(2026, 7, 1))

    # filtrando por datas: antes da data informada
    # mensagens = imb.messages(date__lt = date(2026, 6, 1))

    # filtrando pelas mensagens "selecionadas"/"com estrela marcada"
    # mensagens = imb.messages(flagged = True)

    # filtrando por determinado texto/palavra:
    # mensagens = imb.messages(subject = "bootcamp")

    # filtrando por pasta 
    # mensagens = imb.messages(folder = "nome_pasta")

    # Combinando filtros:
    mensagens = imb.messages(sent_from = "neuron.datagirls@gmail.com",
                             date__gt = date(2026, 7, 1))

    if not mensagens:
        print("Erro ao acessar!")
    else:
         print("Acesso Ok!")

    print(f"Total de mensagens encontradas: {len(mensagens)}")

    for uid, msg in mensagens:
        print(f"De: {msg.sent_from[0]['email']}")
        print(f"Assunto: {msg.subject}")
        print("\n")


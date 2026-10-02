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

    # filtrando por mensagens não lidas
    # mensagens = imb.messages(unread=True)

    mensagens = imb.messages(sent_to= "neuron.datagirls@gmail.com")


    if not mensagens:
        print("Erro ao acessar!")
    else:
         print("Acesso Ok!")

    print(f"Total de mensagens encontradas: {len(mensagens)}")

    for uid, msg in mensagens:
        print(f"De: {msg.sent_from[0]['email']}")
        print(f"Assunto: {msg.subject}")
        print(msg.attachments)

        for anexo in msg.attachments:
            print(anexo['filename'])
            nome_arquivo = anexo['filename']
            conteudo_anexo = anexo['content']

            with open(f"anexos/{nome_arquivo}", "wb") as file:
                file.write(conteudo_anexo.read())
                print("Anexo salvo na pasta!!!")

        print("\n")
from imbox import Imbox
from imbox.settings import Config
import json

with open("credenciais_gmail.json", "r") as file:
    credenciais = json.loads(file.read())

# credenciais
# credenciais["email"]

email = credenciais["email"]
senha = credenciais["password"]
servidor = credenciais["host"]

# conectando ao email:

# Código usado em aula:
# with Imbox('imap.gmail.com',
    # username=email,
    # password=senha) as imb:

# Código alterado para a versão mais nova/ versão que foi instalada:
config = Config(
    username=email,
    password=senha,
    imap_url=servidor,
    ssl=True,
    ssl_context=None,
    starttls=False
)

with Imbox(config) as imb:
    # mensagens = imb.messages()

    # Trazer mensagens que não foram lidas
    mensagens = list(imb.messages(unread=True))
    mensagens.reverse()

    if not mensagens:
        print("Erro ao acessar!")
    else:
        print("Acesso Ok!")

    # print(type(mensagens))
    # len se refere a quantidade de mensagens existentes no email
    # print(len(mensagens))
    print(mensagens[0][1])

    # Acessando o 1º elementos/mensagemn:

    for uid, msg in mensagens:
        print("**** Informações do email: ******")
        print(msg.parsed)
        print(msg.parsed.sent_from)
        print(type(msg.parsed.sent_from))
        print(len(msg.parsed.sent_from))
        print(f"De: {msg.parsed.sent_from[0]['name']} - {msg.parsed.sent_from[0]['email']}")
        print(msg.parsed.date)
        print(f"Assunto: {msg.parsed.subject}")
        print(msg.parsed.body['plain'][0])
        break

# Verificando a quantidade de mensagens não lidas:       
with Imbox(config) as imb:
    nao_lidas = list(imb.messages(unread=True))
    print(f"Total de não lidas: {len(nao_lidas)}")

    # Trás informações das mensagens não lidas:
    for uid, msg in nao_lidas:
        print(uid, "-", msg.parsed.subject)

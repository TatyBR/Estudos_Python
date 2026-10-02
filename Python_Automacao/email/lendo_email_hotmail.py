import msal
import json
import os

from imap_tools import MailBox

with open("credenciais_hotmail.json", "r") as file:
    credenciais = json.loads(file.read())

CLIENT_ID = credenciais["CLIENT_ID"]
AUTHORITY = credenciais["AUTHORITY"]
SCOPES = credenciais["SCOPES"]
EMAIL = credenciais["EMAIL"]
HOST = credenciais["HOST"]
CACHE_FILE = credenciais["CACHE_FILE"]

# login no Hotmail usando MSAL
# app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)
# resultado = app.acquire_token_interactive(SCOPES)
# substituindo o código acima para uso de cache


# Carrega o cache se ele já existir
cache = msal.SerializableTokenCache()

if os.path.exists(CACHE_FILE):
    cache.deserialize(open(CACHE_FILE, "r").read())

# login no Hotmail usando MSAL com cache
app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

# Tenta obter o token do cache sem abrir o navegador
resultado = None
contas = app.get_accounts()
if contas:
    resultado = app.acquire_token_silent(SCOPES, account=contas[0])

# Se não funcionar, mas o login pelo navegador
if not resultado:
    resultado = app.acquire_token_interactive(SCOPES)

# Salva o cache atualizado
if cache.has_state_changed:
    open(CACHE_FILE, "w").write(cache.serialize())


if "access_token" in resultado:
    print("Acesso realizado com sucesso!")
    print("Início do token de acesso:", resultado["access_token"][:20], "...\n")
else:
    print("Falha no acesso.")
    print("Erro:", resultado.get("error"))
    print("Descrição do erro:", resultado.get("error_description"))
    raise SystemExit("Erro ao realizar o login no Hotmail. Verifique as credenciais e tente novamente.\n")

token = resultado["access_token"]

# Conexão IMAP usando o token no lugar da senha

with MailBox(HOST).xoauth2(EMAIL, token) as mailbox:
    for msg in mailbox.fetch(limit=2, reverse=True):
        print("Assunto:", msg.subject)
        print("De:", msg.from_)
        print("Data:", msg.date)
        # print("Corpo:", msg.text or msg.html)
        # print("-" * 50)
        print(msg.date, "|", msg.from_, "|", msg.subject)
        print("\n")
import msal
import json
import os
import requests


with open("credenciais_hotmail.json", "r") as file:
    credenciais = json.loads(file.read())

CLIENT_ID = credenciais["CLIENT_ID"]
AUTHORITY = credenciais["AUTHORITY"]
SCOPES_GRAPH = credenciais["SCOPES_GRAPH"]
CACHE_FILE_GRAPH = credenciais["CACHE_FILE_GRAPH"]

# Cache do token
cache = msal.SerializableTokenCache()
if os.path.exists(CACHE_FILE_GRAPH):
    cache.deserialize(open(CACHE_FILE_GRAPH, "r").read())

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

# Login
resultado = None
contas = app.get_accounts()
if contas:
    resultado = app.acquire_token_silent(SCOPES_GRAPH, account=contas[0])

if not resultado:
    resultado = app.acquire_token_interactive(SCOPES_GRAPH)

if cache.has_state_changed:
    open(CACHE_FILE_GRAPH, "w").write(cache.serialize())

if "access_token" in resultado:
    print("Acesso realizado com sucesso!")
    print("Início do token de acesso:", resultado["access_token"][:20], "...\n")
else:
    print("Falha no acesso.")
    print("Erro:", resultado.get("error"))
    print("Descrição do erro:", resultado.get("error_description"))
    raise SystemExit("Erro ao realizar o login no Hotmail. Verifique as credenciais e tente novamente.\n")

token = resultado["access_token"]

# Requisição à Graph API
url = "https://graph.microsoft.com/v1.0/me/messages"

parametros = {
    "$top": 4,
    "$select": "subject,from,receivedDateTime",
    "$orderby": "receivedDateTime desc",
}

cabecalho = {"Authorization": f"Bearer {token}"}

resposta = requests.get(url, headers=cabecalho, params=parametros)

if resposta.status_code != 200:
    print("Erro ao buscar mensagens.")
    print("Código de status:", resposta.status_code)
    print("Resposta:", resposta.text)
    raise SystemExit("Erro ao buscar mensagens. Verifique a conexão e tente novamente.\n")

for msg in resposta.json()["value"]:
    remetente = msg.get("from", {}).get("emailAddress", {}).get("address", "(sem remetente)")
    print("Assunto:", msg.get("subject"))
    print("De:", remetente)
    print("Data de recebimento:", msg.get("receivedDateTime"))
    print("-" * 50)
    print("\n")
import msal
import json

with open("credenciais_hotmail.json", "r") as file:
    credenciais = json.loads(file.read())

CLIENT_ID = credenciais["CLIENT_ID"]
AUTHORITY = credenciais["AUTHORITY"]
SCOPES = credenciais["SCOPES"]

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

resultado = app.acquire_token_interactive(SCOPES)

if "acess_token" in resultado:
    print("Acesso realizado com sucesso!")
    print("Início do token de acesso:", resultado["access_token"][:20], "...")
else:
    print("Falha no acesso.")
    print("Erro:", resultado.get("error"))
    print("Descrição do erro:", resultado.get("error_description"))
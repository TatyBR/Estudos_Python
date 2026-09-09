import os
import pypdf

# mudando o diretório de trabalho
# o sript será executado dentro deste diretório
os.chdir(r"C:\Taita Geral\1. CURSOS\Estudos_Python\Python_Automacao\arquivos_pdf\dados\relatorios")

# os.listdir()  # listando os arquivos do diretório

pdf_destino = pypdf.PdfWriter()

for arquivo in os.listdir():
    # verificando se o arquivo é um PDF
    # print(arquivo.rsplit("."))

    # realizando desempacotamento:
    nome, extensão = arquivo.rsplit(".")

    # print(nome)
    # print(extensão)

    if extensão.lower() == "pdf":
        # lendo o arquivo PDF
        arquivo_pdf = pypdf.PdfReader(arquivo)

        # lendo todas as páginas do PDF e adicionando no PDF em branco criado anteriormente
        for pagina in arquivo_pdf.pages:
            pdf_destino.add_page(pagina)

# salvando o pdf final
pdf_destino.write("relatorio_consolidado.pdf")
        
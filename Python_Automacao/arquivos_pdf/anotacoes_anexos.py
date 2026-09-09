import pypdf
from pypdf.annotations import FreeText, Text
import os


os.chdir(r"C:\Taita Geral\1. CURSOS\Estudos_Python\Python_Automacao\arquivos_pdf\dados")
pdf = pypdf.PdfWriter(clone_from="o_cortico.pdf")

# acessando as coordenadas da parte em branco da página do pdf
# os dois primeiros números se referem ao ponto superior esquerdo
# os dois últimos se referem ao ponto inferior direito
print(pdf.pages[0].mediabox)


# anotação que será incluída no pdf
# aqui passamos as coordenadas de onde deve ficar o texto livre
texto_livre = FreeText(text="Isto é um texto livre", rect=(50, 50, 400, 400), font_size=20)
pdf.add_annotation(0, texto_livre)

anotacao = Text(text="Isto é uma anotação", rect=(50, 50, 400, 400))
pdf.add_annotation(1, anotacao)


# salvando para testar a inclusão da anotação
pdf.write("pdf_com_anotacao.pdf")

# verificando se o pdf possui anotações
leitor = pypdf.PdfReader("pdf_com_anotacao.pdf")
# quando há anotações, as informações sobre estão dentro de /Annots
leitor.pages[0]['/Annots']

for anotacao in leitor.pages[0]['/Annots']:
    print(anotacao.get_object())
    print(anotacao.get_object()['/Contents'])

# passa por toda a página e procura as anotações
for pagina in leitor.pages:
    if '/Annots' in pagina:
        for anotacao in pagina['/Annots']:
            print(anotacao.get_object())
            print(anotacao.get_object()['/Contents'])

# inserindo um anexo no pdf: que é uma imagem

# 1º lendo o arquivo da imagem em forma binária
with open("coxinha.jpg", "rb") as file:
    imagem = file.read()

# adicionando o anexo no pdf
pdf.add_attachment("coxinha.jpg", imagem)

pdf.write("pdf_com_anexo.pdf")

# extraindo anexos de um pdf
leitor = pypdf.PdfReader("pdf_com_anexo.pdf")

# isso é uma lista:
# leitor.attachments['coxinha.jpg'][0]

# quando não sei o nome dos anexos, poso usar:
# for anexo in leitor.attachments:
    # print(anexo)

# cria a pasta se não existir; não dá erro se já existir
# os.makedirs('anexos', exist_ok=True)   

for anexo in leitor.attachments:
    arquivo = leitor.attachments[anexo][0]

    # extrai o anexo e o salva na pasta: anexos
    with open(f'anexos/{anexo}', 'wb') as file:
        file.write(arquivo)
    
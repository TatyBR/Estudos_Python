import pypdf
import os

os.chdir(r"C:\Taita Geral\1. CURSOS\Estudos_Python\Python_Automacao\arquivos_pdf\dados")


pdf = pypdf.PdfWriter(clone_from="o_cortico.pdf")

# Protegendo o pdf com senha
pdf.encrypt(user_password="112233")

# salvado para testar o uso da senha
pdf.write("pdf_protegido.pdf")

# lendo arquivos pdf com senha
leitor = pypdf.PdfReader("pdf_protegido.pdf")

# inserindo a senha para abrir o arquivo
leitor.decrypt("112233")

leitor.pages[0]
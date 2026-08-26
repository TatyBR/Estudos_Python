import pypdf

# lendo um arquivo PDF
arquivo_pdf = pypdf.PdfReader("dados/o_cortico.pdf")

# type: class
print(type(arquivo_pdf))

# Verificando a quantidade de páginas do PDF
print(arquivo_pdf.pages)    # lista de PageObjects
print(len(arquivo_pdf))
print(arquivo_pdf.pages[4])

# percorrendo todas as páginas do PDF
for pagina in arquivo_pdf.pages:
    print(pagina)


# Metadados de um PDF (Author, Creator....)
print(arquivo_pdf.metadata)
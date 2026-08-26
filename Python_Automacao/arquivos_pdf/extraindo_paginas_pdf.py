import pypdf

# lendo um arquivo PDF
arquivo_pdf = pypdf.PdfReader("dados/o_cortico.pdf")

# Escrevendo um PDF/ cria um pdf em branco
pdf_destino = pypdf.PdfWriter()

# Extraindo uma pagina de um PDF
pagina01 = arquivo_pdf.pages[0]
pagina01

# adicionando a pagina extraída do PDF no PDF em branco criado anteriormente
pdf_destino.add_page(pagina01)

# salvando o novo PDF
pdf_destino.write("dados/pagina01.pdf")

# extraindo diversas páginas
num_paginas = [9, 14, 19]

for pagina in num_paginas:
    pdf_destino.add_page(arquivo_pdf.pages[pagina])

pdf_destino.write("dados/paginas_extras.pdf")
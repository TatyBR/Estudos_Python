import pypdf

leitor = pypdf.PdfReader("dados\o_cortico.pdf")

# print(leitor.pages[0].extract_text()[0:20])

textos = []
# extraindo todo o texto do pdf
for pagina in leitor.pages:
    textos.append(pagina.extract_text())
textos


texto_completo = ''.join(textos)
print(texto_completo)


# usando list comprehension:

textos2 = [pagina.extract_text() for pagina in leitor.pages]
print(textos2)

leitor_ambev = pypdf.PdfReader(r"dados\ambev.pdf")


print(leitor_ambev.pages[0].extract_text())
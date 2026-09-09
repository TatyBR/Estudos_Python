import pypdf

leitor = pypdf.PdfReader(r"dados\ambev.pdf")

# lista as imagens existentes na primeira página do pdf
# usando imagem.data acessamos o conteudo binário de cada imagem
# for imagem in leitor.pages[0].images:
    # print(imagem)

# lendo a página 1 do pdf e extraindo todas as imagens existentes:
for imagem in leitor.pages[0].images:
    with open(f"dados/imagens/{imagem.name}", "wb") as file:
        file.write(imagem.data)


# lendo todo o arquivo pdf e extraindo todas as imagens existentes:
for pagina in leitor.pages:
    for imagem in pagina.images:
        with open(f"dados/imagens/{imagem.name}", "wb") as file:
            file.write(imagem.data)
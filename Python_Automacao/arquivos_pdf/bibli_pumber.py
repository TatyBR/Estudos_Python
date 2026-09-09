import pdfplumber

pdf = pdfplumber.open("dados/sebrae.pdf")

texto = pdf.pages[10].extract_text()
print(texto)

texto = pdf.pages[13].extract_text()
print(texto)

# página com tabela
# extract_tables(): trás uma lista com todas as tabelas da página   
# extract_table(): se houver várias tabelas, trás a maior delas
# extrai dados linha a linha....
tabela = pdf.pages[29].extract_table()
tabela

# Aqui é gerado uma lista de tabelas:
tabelas = pdf.pages[29].extract_tables()
# Selecionando a segunda tabela:
tabelas[1]
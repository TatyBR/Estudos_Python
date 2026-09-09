# modificar o conteúdo de um pdf: fazer um clone dele.

import pypdf
import os

os.chdir(r"C:\Taita Geral\1. CURSOS\Estudos_Python\Python_Automacao\arquivos_pdf\dados")
pdf = pypdf.PdfWriter(clone_from="o_cortico.pdf")

# um pequeno teste.....
# for pagina in pdf.pages:
    # extrai o texto da página
    # print(pagina.extract_text())

tranf_pdf = pypdf.Transformation()

# rotacionando o conteúdo do pdf
pdf.pages[0].add_transformation(tranf_pdf
                                .rotate(30)
                                .translate(tx=400))

# movendo o conteúdo do pdf para os lados
pdf.pages[1].add_transformation(tranf_pdf
                                .translate(tx=400, ty=500))

# alterar a escala do conteúdo do pdf
pdf.pages[2].add_transformation(tranf_pdf
                                .scale(sx=0.5, sy=0.5))

# alterar a escala da pagina!!!
pdf.pages[3].scale_by(1.5)


# salvado para verificar a rotacao
pdf.write("pdf_modificado.pdf")




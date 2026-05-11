# %%
# instalar o wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# %%
# lendo arquivo txt
with open ('wordcloud/elefante.txt', 'r', encoding='utf8') as file:
    texto = file.read()

# %%
print(texto)

# %%
wc = WordCloud(height=200,
               width=600)
nuvem = wc.generate(texto)

# plotando a nuvem de palavras
plt.imshow(nuvem)
plt.axis('off')
plt.show()

# %%
# Stopwords: palavras que não quero que apareçam na nuvem

stopwords = ['o','a','um','uma','ã','e','ela','ele','não','mas','que','ao','por','ali','os','as','de','da','do']
wc = WordCloud(height=200,
               width=600,
               stopwords=stopwords)
nuvem = wc.generate(texto)
plt.imshow(nuvem)
plt.axis('off')
plt.show()

# %% 

# Criando uma máscara: é possível usar o formato de alguma imagem
# imagem em png e toda preta
# para usar a imagem como máscara: converter em array

from PIL import Image
import numpy as np

imagem = Image.open('wordcloud/elefante.png')
plt.imshow(imagem)
plt.axis('off')
plt.show()

# %%

mascara = np.array(imagem)
# mascara.shape

# %%
nuvem = wc.generate(texto)
wc = WordCloud(mask=mascara, 
               background_color='white',
               stopwords=stopwords
               # contour_color='blue',
               # contour_width=1
               )
plt.imshow(nuvem)
plt.axis('off')
plt.show()

# %%


from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

palavras = "Machine Learning IA  LLM Data Lakehouse Data Mesh Governança Storytelling Data Product Pipeline Edge AI Análise LGPD Engenharia Ciência Python SQL Excel Pandas"
imagem = Image.open('wordcloud/python.png')
mascara_imag = np.array(imagem)
wc = WordCloud(mask=mascara_imag, 
               background_color='white',
               contour_color='black',
               contour_width=1)
nuvem = wc.generate(palavras)
plt.imshow(nuvem)
plt.axis('off')
plt.show()

# %%


from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

palavras = "Machine Learning IA  LLM Data Lakehouse Data Mesh Governança Storytelling Data Product Pipeline Edge AI Análise LGPD Engenharia Ciência Python SQL Excel Pandas"
imagem = Image.open('nuvem.png')
mascara_imag = np.array(imagem)
mascara_invertida = 255 - mascara_imag
wc = WordCloud(mask=mascara_imag, 
               background_color='white',
               contour_color='black',
               contour_width=1)
nuvem = wc.generate(palavras)
plt.imshow(nuvem)
plt.axis('off')
plt.show()

# %%

from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

palavras = "Machine Learning IA  LLM Data Lakehouse Data Mesh Governança Storytelling Data Product Pipeline Edge AI Análise LGPD Engenharia Ciência Python SQL Excel Pandas"
imagem = Image.open('nuvem.png')
mascara_imag = np.array(imagem)
mascara_invertida = 255 - mascara_imag
wc = WordCloud(mask=mascara_invertida, 
               background_color='white',
               contour_color='green',
               contour_width=1)
nuvem = wc.generate(palavras)
plt.imshow(nuvem)
plt.axis('off')
plt.show()



# %%

from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

palavras = "Machine Learning IA  LLM Data Lakehouse Data Mesh Governança Storytelling Data Product Pipeline Edge AI Análise LGPD Engenharia Ciência Python SQL Excel Pandas"

wc = WordCloud(height=800,
               width=800)
nuvem = wc.generate(palavras)

plt.imshow(nuvem)
plt.axis('off')
plt.show()

# como pesquisar no google por imagem: cloud silhouette black png
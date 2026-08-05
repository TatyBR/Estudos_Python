#%%
lista1 = [10, 20, 30, 40]
lista2 = ['Hello World', 10, 20, 30, [1, 2, 3], (45, 50)]
type(lista1)

#%%

# Acessando os elementos da lista
lista3 = ['A', 'B', 'C']
print(lista3[0])  # A
print(lista3[2])  # C
print(lista3[-1])  # C

#%%

# Modificando elementos da lista
lista3[1] = 'D'
print(lista3)  # ['A', 'D', 'C']
print(len(lista3))  # 3

# %%
num = [31, 914, 236, 376, 140, 705]

print(f"Valor máximo da lista: {max(num)}")
print(f"Valor mínimo da lista: {min (num)}")
print(f"Número de elementos da lista: {len(num)}")
print(f"Soma de elementos da lista: {sum(num)}")

# %%

# Unindo listas
lista4 = [1, 2, 3]
lista5 = [4, 5, 6]
lista6 = lista4 + lista5
print(lista6)  # [1, 2, 3, 4, 5, 6]

lista7 = ['a', 'b', 'c']
lista8 = ['x', 'y', 'z']
uniao = lista7 + lista8
print(uniao)  # ['a', 'b', 'c', 'x', 'y', 'z']  


# %%

# Repetindo elementos da lista
lista9 = [1, 2, 3]
lista9*4

# %%

# Construtor lista
tupla = (1, 2, 3, 4)
print(type(tupla))  # <class 'tuple'>
lista10 = list(tupla)
print(lista10)  # [1, 2, 3, 4]
print(type(lista10))  # <class 'list'>
# %%

# Criando uma lista com range()
lista11 = list(range(2010, 2021))
print(lista11)  # [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# %%

# Convertendo uma str em uma lista
string = 'Python é uma linguagem de programação'

# Converte em uma lista e separa os elementos pelo espaço
lista12 = string.split(sep=' ')
print(lista12)  # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

py = '%Python%Python%Python%Python%Python'
py.split(sep='%')  # ['', 'Python', 'Python', 'Python', 'Python', 'Python']

# %%

# Definindo uma lista a partir de variáveis
num1 = 10
num2 = 20
num3 = 30
lista13 = [num1, num2, num3]
print(lista13)  # [10, 20, 30]

# %%

# Desempacotando uma lista
lista14 = [340, 4500, 900, "Python"]
a, b, c, d = lista14
print(a)  # 340
print(b)  # 4500
print(c)  # 900
print(d)  # Python

# %%

# Fatiamento de listas (slincing)
z = [4, 7, 9, 11, 3, 1]
print(z[:4])  # [4, 7, 9]
print(z[3:6])  # [11, 3, 1]
print(z[:3])   # [4, 7, 9]
print(z[3:])   # [11, 3, 1]

# %%

# Verificando se um elemento está presente na lista
lista15 = ['s', 't', 'u', 'v', 'w']

print('u' in lista15)  # True

print('a' in lista15)  # False

# %%

# Métodos em listas
# append() - Adiciona um elemento ao final da lista
# insert() - Adiciona um elemento em uma posição específica da lista
# extend() - Adiciona elementos de outra lista ao final da lista
# pop() - Remove e retorna o último elemento da lista
# remove() - Remove o primeiro um elemento da lista com o valor especificado
# clear() - Remove todos os elementos da lista
# copy() - Retorna uma cópia da lista
# sort() - Ordena os elementos da lista em ordem crescente
# reverse() - Inverte a ordem dos elementos da lista
# index() - Retorna o índice do primeiro elemento com o valor especificado
# count() - Conta o número de vezes qiue o elemento aparece na lista

# %%
numeros =[20, 30, 40, 50, 60]
numeros.append(100)
numeros

numeros.extend([2, 4])
numeros

# %%

# insere o número 75 na posição 2 da lista
numeros.insert(2, 75)
numeros
# %%

numeros.pop()  # Remove o último elemento da lista
numeros

numeros.pop(4)
numeros

# %%

# Deletando elementos com del

letras = ['k', 'l', 'm', 'n', 'o']
del letras[2]
letras

# Deletando toda a lista
del letras
letras

# %%

# Removendo todos os elementos da lista

letras = ['j', 'k', 'l', 'm', 'n', 'o']
letras.clear()
letras

# %%

# Retorna a quantidade de vezes que o elemento aparece na lista
lista16 = [10, 20, 30, 30, 40, 40 ,50]
lista16.count(30)  # Retorna 2
# %%

# Inverte a ordem da lista
lista16.reverse()
lista16

# %%

# Ordena a lista em ordem crescente
lista17 = [80, 20, 70, 30, 95, 82]
lista17.sort()
lista17

# %%

lista17.index(30)  # Retorna o índice do primeiro elemento com o valor 30
lista16.index(40,2)  # Retorna o índice do primeiro elemento com o valor 40 a partir do índice 2

# %%



# %%

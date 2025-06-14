import numpy as np

# Desafio 1:
# 1. Crie um array de 20 elementos.
array = np.arange(1, 21)
print(array)

# 2. Extraia os primeiros 5 elementos, os últimos 5 
# elementos e os elementos 
# das posições 5 a 10.
print('primeiros 5 ', array[:5])
print('ultimos 5 ', array[-5:])
print('5 a 10', array[5:10])

# Desafio 2:
# 1. Crie duas matrizes 3x3.
# 2. Calcule o produto.
matriz1 = np.random.randint(1, 10, (3, 3))
matriz2 = np.random.randint(1, 10, (3, 3))
produto = np.dot(matriz1, matriz2)
print('produto = ', produto)


# Desafio 3:
# Criação de Arrays:


# Crie um array de 1 a 10.
# Crie uma matriz 3x3 com valores aleatórios entre 0 e 1.
array_ = np.arange(1, 11)
matriz_aleaoria = np.random.randint(1, 100, (3, 3))
print('array de 1 a 10:', array_)
print('matriz 3x3 aleatória:\n', matriz_aleaoria)

# Desafio 4:
# Calcule a soma dos elementos do array.
# Encontre o valor máximo e mínimo do array.
soma = np.sum(array_)
maximo , minimo = np.max(array_), np.min(array_)
print('soma dos elementos do array:', soma)
print('valor máximo do array:', maximo)

# Desafio 5:
# Calcule a média dos valores do array.
# Calcule a mediana dos valores do array.
media = np.mean(array_)
mediana = np.median(array_)
print('média dos valores do array:', media)
print('mediana dos valores do array:', mediana)


# Desafio 6:
# Adicione 10 a todos os elementos do array.
# Reshape o array 1D para um array 2D (2x5).
array_adicionar = array_ + 10
array_reshape = array_adicionar.reshape(2, 5)
print('array com 10 adicionado a todos os elementos:', array_adicionar)
print('array 2D (2x5):\n', array_reshape)



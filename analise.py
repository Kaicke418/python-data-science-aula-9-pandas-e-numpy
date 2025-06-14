import statistics as sts

def media(lista):
    return sum(lista)/len(lista)

def moda(lista):
    return sts.mode(lista)

def mediana (lista):
    return sts.median(lista)

def desvio(lista):
    return sts.stdev(lista)

def amplitude(lista):
    return max(lista) - min(lista)

def variancia(lista):
    return sts.variance(lista)

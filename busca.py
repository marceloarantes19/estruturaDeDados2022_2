def buscaSequencial(x, valor):
  n = len(x)
  for i in range(0, n):
    if x[i] == valor:
      return i
  return -1

def buscaBinaria(x, valor):
  limiteInferior = 0
  limiteSuperior = len(x) - 1
  while limiteInferior <= limiteSuperior:
    posicaoAtual = (limiteInferior + limiteSuperior)//2
    if valor == x[posicaoAtual]:
      return posicaoAtual
    elif valor < x[posicaoAtual]:
      limiteSuperior = posicaoAtual - 1
    else:
      limiteInferior = posicaoAtual + 1
  return -1

k = [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 25]
v = 24
indice = buscaBinaria(k, v)
if indice > -1:
  print(v, "está na posição", indice)
else:
  print(v, "não se encontra no vetor")
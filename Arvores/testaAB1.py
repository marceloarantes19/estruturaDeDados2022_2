from Elemento import Elemento 
from ArvoreBB import ArvoreBB
a = ArvoreBB()
c = int(input("Digite uma chave (-1 encerra): "))
while c != -1:
  n = input("Digite um nome: ")
  elem = Elemento(c, n)
  a.insereNo(elem)
  a.emOrdem(a.getRaiz())
  c = int(input("Digite uma chave (-1 encerra): "))

print("arvore final: ")
a.emOrdem(a.getRaiz())

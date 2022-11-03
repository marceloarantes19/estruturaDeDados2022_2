from Elemento import Elemento 
from ArvoreBB import ArvoreBB
x = [10, 7, 16, 3, 12, 20, 1, 5, 14, 17]
a = ArvoreBB()
for i in x:
  elem = Elemento(i)
  a.insereNo(elem)
print("arvore Em ordem: ")
a.emOrdem(a.getRaiz())
print("\narvore Pré ordem: ")
a.preOrdem(a.getRaiz())
print("\narvore Pós ordem: ")
a.posOrdem(a.getRaiz())
print("arvore Em ordem decrescente: ")
a.ordemDecrescente(a.getRaiz())

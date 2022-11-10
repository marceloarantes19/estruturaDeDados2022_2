from Elemento import Elemento 
from ArvoreBB import ArvoreBB
x = [20, 3, 22, 1, 10, 24, 7, 17, 23, 26, 9, 15, 25, 12, 16]
a = ArvoreBB()
for i in x:
  elem = Elemento(i)
  a.insereNo(elem)

a.retira(20)
#a.retira(3)
#a.retira(25)

print("arvore Em ordem: ")
a.emOrdem(a.getRaiz())

'''print("\narvore Pré ordem: ")
a.preOrdem(a.getRaiz())
print("\narvore Pós ordem: ")
a.posOrdem(a.getRaiz())
print("\narvore Em ordem decrescente: ")
a.ordemDecrescente(a.getRaiz())
print("14 Está na árvore?", a.achaValorABB(a.getRaiz(), 14))
print("8 Está na árvore?", a.achaValorABB(a.getRaiz(), 8))
print("Quantidade de Nós na árvore:", a.contaNos(a.getRaiz()))
'''
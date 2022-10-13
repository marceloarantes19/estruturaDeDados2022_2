from PilhaEncadeada import PilhaEncadeada
from Elemento import Elemento 
from No import No
p = PilhaEncadeada()
n = int(input("Digite um número inteiro positivo: "))
x = ""
while n > 0:
  elem = Elemento(n%2,"")
  no = No(elem)
  p.push(no)
  n = n // 2

while not p.pilhaVazia():
  x = x + str(p.pop().getInfo().getChave())

print(x)
from Pilha import Pilha
p = Pilha()
n = int(input("Digite um número inteiro positivo: "))
x = ""
while n > 0:
  p.push(n % 2)
  n = n // 2

while not p.pilhaVazia():
  x = x + str(p.pop())

print(x)

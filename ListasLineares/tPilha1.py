from Pilha import Pilha
pilha = Pilha()
x = input("Digite um nome: ")
for i in x:
  pilha.push(i)
x = ""
while(not pilha.pilhaVazia()):
  x = x + pilha.pop()

print(x)
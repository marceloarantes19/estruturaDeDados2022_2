from Fila import Fila 
def menu():
  print("1 - Enfileira")
  print("2 - Desenfileira")
  print("3 - Mostar fila")
  print("0 - Sair")
  return int(input("Digite uma opção: "))
f = Fila()
op = 1
while op > 0:
  x = menu()
  if x == 1:
    v = int(input("Digite um valor: "))
    f.enQueue(v)
  elif x == 2:
    print("Saiu da fila:", f.deQueue())
  elif x == 3:
    f.mostraInfo()
  else:
    op = 0
from Elemento import Elemento
from No import No
from ListaEncadeada import ListaEncadeada

l = ListaEncadeada()
chave = int(input("Digite uma chave (-1 para sair): "))
while chave != -1:
  nome = input("Digite um nome: ")
  elem = Elemento(chave, nome)
  no   = No(elem)
  l.insereNoInicio(no)
  print("\n*** Apresentando a lista ***")
  l.mostraListaRec(l.getCabeca().getProx())
  chave = int(input("Digite uma chave (-1 para sair): "))
l.mostraListaInv(l.getCabeca().getProx())

print("**** Total de elementos na lista: ", l.len2(l.getCabeca().getProx()))
print("\n\n*** Retirando todos os Nós***")
while not l.listaVazia():
  no = l.retiraNoInicio()
  print(no.getInfo().getChave()," - ", no.getInfo().getNome())


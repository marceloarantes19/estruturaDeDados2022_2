from No import No
class ListaEncadeada:
  def __init__(self):
    self.__cabeca = No()
  def getCabeca(self):
    return self.__cabeca
  def setCabeca(self, c):
    self.__cabeca = c 
  def listaVazia(self):
    return self.getCabeca().getProx() == None
  def insereNoInicio(self, n): # n é um objeto da classe No
      n.setProx(self.getCabeca().getProx())
      self.getCabeca().setProx(n)
  def retiraNoInicio(self):
    if not self.listaVazia():
      ret = self.getCabeca().getProx()
      self.getCabeca().setProx(ret.getProx())
      ret.setProx(None)
      return ret 
  def insereNoFim(self, n):
    ant = self.getCabeca()
    atual = self.getCabeca().getProx()
    while atual != None:
      ant = atual
      atual = ant.getProx()
    ant.setProx(n)
  def retiraNoFim(self):
    if not self.listaVazia():
      ant = self.getCabeca()
      atual = self.getCabeca().getProx()
      while atual.getProx() != None:
        ant = atual
        atual = ant.getProx()
      ant.setProx(None)
      return atual
  def mostraLista(self):
    atual = self.getCabeca().getProx()
    while atual != None:
      print(atual.getInfo().getChave())
      atual = atual.getProx()
  def mostraListaRec(self, no):
    if no != None:
      print(no.getInfo().getElemento())
      self.mostraListaRec(no.getProx()) 
    
  def mostraListaInv(self, no):
    if no != None:
      self.mostraListaInv(no.getProx()) 
      print(no.getInfo().getElemento())

  def len(self):
    ret = 0
    atual = self.getCabeca().getProx()
    while atual != None:
      ret = ret + 1
      atual = atual.getProx()
    return ret
  def len2(self, no):
    return 0 if no == None else 1 + self.len2(no.getProx())



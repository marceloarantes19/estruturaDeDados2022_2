from Elemento import Elemento
from NoABB import NoABB
class ArvoreBB:
  def __init__(self):
    self.__raiz = None 
  def getRaiz(self):
    return self.__raiz
  def setRaiz(self, r):
    self.__raiz = r
  def arvoreVazia(self):
    return self.__raiz == None
  def criaNo(self, elemento):
    no = NoABB(elemento)
    return no
  def insereNo(self, el):
    if self.arvoreVazia():
      self.setRaiz(self.criaNo(el))
    else:
      self.insere(None, self.getRaiz(), el)
  def insere(self, pai, atual, el):
    if atual == None:
      if el.getChave()<pai.getElemento().getChave():
        pai.setFE(self.criaNo(el))
      else:
        pai.setFD(self.criaNo(el))
    elif el.getChave() < atual.getElemento().getChave():
      self.insere(atual, atual.getFE(), el)
    else:
      self.insere(atual, atual.getFD(), el)
  def emOrdem(self, n):
    if n != None: 
      self.emOrdem(n.getFE())
      print(n.getElemento().getElemento())
      self.emOrdem(n.getFD())
  def preOrdem(self, n):
    if n != None: 
      print(n.getElemento().getElemento())
      self.preOrdem(n.getFE())
      self.preOrdem(n.getFD())
  def posOrdem(self, n):
    if n != None: 
      self.posOrdem(n.getFE())
      self.posOrdem(n.getFD())
      print(n.getElemento().getElemento())

  # Resolucao dos exercícios
  def ordemDecrescente(self, n):
    if n != None: 
      self.ordemDecrescente(n.getFD())
      print(n.getElemento().getElemento())
      self.ordemDecrescente(n.getFE())
  
  def achaValorABB(self, n, v):
    if n != None:
      if v == n.getElemento().getChave():
        return True 
      elif v < n.getElemento().getChave():
        return self.achaValorABB(n.getFE(), v)
      else:
        return self.achaValorABB(n.getFD(), v)
    return False

  def contaNos(self, n):
    if n != None: 
      return 1 + self.contaNos(n.getFE()) + self.contaNos(n.getFD())
    return 0



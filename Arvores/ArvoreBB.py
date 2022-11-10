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
  # Como retirar nó da árvore
  def retira(self, v):
    return self.retiraNoTriv(None, self.getRaiz(), v)
  def retiraNoTriv(self, pai, atu, v):
    if atu == None:
      return None
    if atu.achouChave(v):
      ret = atu
      # Se o no a apagar é folha:
      if atu.eFolha():
        if pai == None: # Esse nó é o raiz e único da árvore
          self.setRaiz(None)
        elif atu.eFE(pai):
          pai.setFE(None)
        else:
          pai.setFD(None)
      elif atu.temDoisF():
        return self.retiraNoNaoTriv(None, atu.getFE(), atu)
      elif atu.temFE():
        if atu == self.getRaiz():
          self.setRaiz(atu.getFE())
        elif atu.eFE(pai):
          pai.setFE(atu.getFE())
        else:
          pai.setFD(atu.getFE())
        atu.setFE(None)
      else:
        if atu == self.getRaiz():
          self.setRaiz(atu.getFD())
        elif atu.eFE(pai):
          pai.setFE(atu.getFD())
        else:
          pai.setFD(atu.getFD())
        atu.setFD(None)
      return ret
    elif atu.chaveMenor(v):
      return self.retiraNoTriv(atu, atu.getFD(), v)
    else:
      return self.retiraNoTriv(atu, atu.getFE(), v)
  def retiraNoNaoTriv(self, pai, atu, fixo):
    if atu.getFD()!=None:
      return self.retiraNoNaoTriv(atu, atu.getFD(), fixo)
    else: 
      x = fixo.getElemento()
      fixo.setElemento(atu.getElemento())
      atu.setElemento(x)
      if pai != None:
        pai.setFD(atu.getFE())
      else:
        fixo.setFE(atu.getFE())
      atu.setFE(None)
      return atu
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



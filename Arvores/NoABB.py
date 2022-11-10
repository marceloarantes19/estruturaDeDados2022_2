from tkinter import E
from Elemento import Elemento
class NoABB:
  def __init__(self, elemento = Elemento()):
    self.__elemento = elemento
    self.__fe = None # Filho a esquerda do nó 
    self.__fd = None # Filho a direita do nó
  def getElemento(self):
    return self.__elemento
  def setElemento(self, e):
    self.__elemento = e 
  def getFE(self):
    return self.__fe 
  def setFE(self, fe):
    self.__fe = fe 
  def getFD(self):
    return self.__fd 
  def setFD(self, fd):
    self.__fd = fd 
  def eFolha(self):
    return self.getFE() == None and self.getFD() == None
  def temFE(self):
    return self.getFE() != None 
  def temFD(self):
    return self.getFD() != None
  def temDoisF(self):
    return self.temFE() and self.temFD()
  def eFE(self, no):
    return no.getFE() == self
  def eFD(self, no):
    return no.getFD() == self
  def achouChave(self, valor):
    return self.getElemento().getChave() == valor
  def chaveMenor(self, valor):
    return self.getElemento().getChave() < valor
  def chaveMaior(self, valor):
    return self.getElemento().getChave() > valor


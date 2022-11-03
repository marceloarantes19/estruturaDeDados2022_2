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



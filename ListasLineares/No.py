class No:
  def __init__(self, info = None):
    self.__info = info if info != None else None 
    self.__prox = None 
  def getInfo(self):
    return self.__info 
  def setInfo(self, info):
    self.__info = info
  def getProx(self):
    return self.__prox
  def setProx(self, p):
    self.__prox = p
  
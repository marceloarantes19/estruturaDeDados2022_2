class Pilha:
  def __init__(self):
    self.__info = []
  
  def pilhaVazia(self):
    return len(self.__info) == 0

  def push(self, dado):
    self.__info.append(dado)

  def pop(self):
    if not self.pilhaVazia():
      return self.__info.pop()
    else:
      return None 

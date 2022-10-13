from ListaEncadeada import ListaEncadeada 
class PilhaEncadeada(ListaEncadeada):
  def pilhaVazia(self):
    return self.listaVazia()
  
  def push(self, no):
    self.insereNoInicio(no)
  
  def pop(self):
    return self.retiraNoInicio()
    
from ListaEncadeada import ListaEncadeada 
class FilaEncadada(ListaEncadeada):
  def filaVazia(self):
    return self.listaVazia() 

  def enQueue(self, no):
    self.insereNoFim(no)
  
  def deQueue(self):
    return self.retiraNoInicio()
  
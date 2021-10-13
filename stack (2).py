"implementacao de uma pilha em python"

class Stack:
  "classe que representa uma pilha"
  def __init__(self):
    "construtor da classe Stack"
    self.elements = []

  def isEmpty(self):
      "retorna verdadeiro caso a pilha esteja vazia"
      return len(self.elements) == 0

  def push(self, value):
      "adiciona uma elemento na pilha"
      self.elements.insert(0, value)

  def pop(self):
      "retorna o elemento do topo da pilha" 
      return self.elements[0] # o que fazer quando a lista estiver vazia?
  
  def size(self):
      "retorna o numero de elementos da pilha" 
      return len(self.elements)

  def clear(self):
      "remove todos os elementos da pilha. util particularmente para testes"
      elements = [] 

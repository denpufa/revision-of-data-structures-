class Lista:
  def __init__(self) :
    self.lista = []
    self.tamanho = 0
  
  """O(1)"""
  def insercaoNoFim(self,elemento):
    self.lista.append(elemento)
    self.tamanho += 1

  """O(n)"""
  def insercaoPorIndex(self,elemento,index):
    listaAux = self.lista[:index] #parte antes do elemento
    listaAux.append(elemento) #add o elemento
    listaAux.extend(self.lista[index:]) #parte depois do elemento
    self.lista = listaAux
    self.tamanho += 1
  
  """O(n)"""
  def remocaoNoFim(self):
    #O(n) -1 
    self.lista = self.lista[:-1]
    self.tamanho -= 1
  
  """O(n)"""
  def remocaoPorIndex(self,index) :
    if index == 0 :
      self.lista =  [
        self.lista[x] for x in range(self.tamanho) if x != 0
        ]      
    elif index == self.tamanho -1 :
        self.remocaoNoFim()
    else :
      self.lista = [
        self.lista[x] for x in range(self.tamanho) if x!= index
      ]
    self.tamanho -= 1 
  
  """O(1)"""
  def buscarUsandoIndex(self,index):
       return self.lista[index]
  
  """O(n) retorna o index""" 
  def buscarUsandoElemento(self,elemento):
    for x in range(self.tamanho):
      if self.lista[x] == elemento:
        return x


"""teste unitário"""
b = Lista()

b.insercaoNoFim(5)
print(b.lista)

b.insercaoPorIndex(3,0)
print(b.lista)

print(b.buscarUsandoIndex(0))
print(b.buscarUsandoElemento(5))

b.remocaoNoFim()
print(b.lista)

b.remocaoPorIndex(0)
print(b.lista)










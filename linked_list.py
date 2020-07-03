from node import Node

"""whitout using exception or better names in python context,just studying"""
class Linked_list :
  def __init__(self) :
    self.head = Node()
    self._size = 0

  #O(n) for any case 
  def append(self,val) -> None :
      pointer = self.head
        if pointer :
          while pointer.next :
            pointer = pointer.next
            pointer.next = Node()
          pointer.next.item = val
        else:
          head.item = val
      self.size += 1    

  #O(n) worst case
  def insert(self,index,val) -> bool :
    pointer = self.head
      if index > self._zise or index < 0 : return False
      if pointer :
        for i in range(index) :
          pointer = pointer.next
      
        reference = pointer.next
        pointer.next = Node()
        pointer.next.item = val
        pointer.next.next = reference
        self.size += 1
        return True
  
  #O(n) worst case 
  def __setitem__(self,index,val) -> bool :
    pointer = self.head
    if index > self.size or index<0 : return False 
    for x in range(index+1) :
      pointer = pointer.next
    pointer.item = val
    return True
  
  #O(n) worst case 
  def __getitem__(self,index) :
    pointer = self.head
    if index > self.size or index<0 : return "index not found"
    for x in range(index+1) :
      pointer = pointer.next
    return pointer.item

  #O(n) worst case 
  def search(self,item)  :
    pointer = self.head
    while pointer.next :
      if pointer.item == item : return item 
      pointer = pointer.next
    return 'not found'
  
  #O(n) worst case 
  def remove_index(self,index) -> bool :
      if index > self.size or index < 0 : return False
      pointer = self.head
      for x in range(index+1):
        pointer = pointer.next
      pointer.next = pointer.next.next
      return True
  
  #O(1) 
  def remove_start(self) :
    if self.head :
      head = head.next
  
 #O(n) worst case 
  def remove_end(self) :
    if self.head :
      pointer = self.head
      while pointer.next.next :
        pointer = pointer.next
      pointer.next = None
  






      






    

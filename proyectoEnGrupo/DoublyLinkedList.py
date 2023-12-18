#fsefasdfesfasdfesfasdf
from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current= None

    def is_empty(self):
        return self.head is None

    def append(self, song_info):
        new_node = Node(song_info)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return popped_data
    
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
        #----------------------------------------------------------
        #-----------------------------------NUEVOS METODOS
        #----------------------------------------------------
    def avanzar(self):
        if self.is_empty():
            return None

        # Al avanzar, si estamos en el último nodo, regresamos al primero
        if self.current == self.tail:
            self.current = self.head
        else:
            self.current = self.current.next

        return self.current.data

    def retroceder(self):
        if self.is_empty():
            return None

        # Al retroceder, si estamos en el primer nodo, vamos al último
        if self.current == self.head:
            self.current = self.tail
        else:
            self.current = self.current.prev

        return self.current.data
    

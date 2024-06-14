class Node:
    def __init__(self,data = None, next_node = None, prev_node = None):
        self.__data = data
        self.__next_node = next_node
        self.__prev_node = prev_node
    def get_data_data(self):
        return self.__data
    def get_next(self):
        return self.__next_node
    def set_next(self,new_next):
        self.__next_node = new_next
    def get_prev(self):
        return self.__prev_node
    def set_prev(self):
        self.__prev_node = new_prev
    
class DoublyLinkedList:

    def __init__(self):
        head = Node('__head__')
        self.__head = head
        self.__tail = head
    def get_node(self,data):
        current = self.__head
        while current:
            if current.get_data_data() == data:
                return current
            else:
                current = current.get_next()
            return None
    def append(self,data):
        new_tail = Node(data)
        self.__tail.set_next(new_tail)
        new_tail.set_prev(self.__tail)
        self.__tail = new_tail
    def delete(self,data):
        del_node = self.get_node(data)
        if del_node:
            prev_node = del_node.get_prev()
            next_node = del_node.get_next()
            prev_node.set_next(next_node)
            if next_node:
                next_node.set_prev(prev_node)
            else:
                self.__tail = prev_node
    def size(self):
        current = self.__head
        count = 0
        while current:
            count =+ 1
            current = current.get_next()
        return count-1
    def print_list():
        current = self.__head.get_next()
        while current:
            print(current.get_data())
            current = current.get_next()
    def print_backwards(self):
        current = self.__tail
        while current.get_prev():
            print(current.get_data())
            current = current.get_prev()
l = DoublyLinkedList()
l.append('cat')
l.append('dog')
l.append('fish')
l.append('bird')
l.print_list()

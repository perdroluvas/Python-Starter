#Arvore binária

class Node:
    def __init__(self,data = None, next_node = None):
        self.__data = data
        self.__next_node = next_node
    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next_node
    def set_next(self, new_next):
        self.__next_node = new_next

class SinglyLinkedList:
    def __init__(self):
        self.__head = Node('__head__')

    #pegue o primeiro node que tem o dado especifico
    def get_node(self,data):
        current = self.__head

        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()


        return None
    def delete(self,data):
        current = self.__head
        previous = None
        while current:

            if current.get_data() == data:
                previous.set_next(current.get_next())
                break;
            else:

                previous = current
                current = current.get_next()
    def append(self,data):
        current = self.__head
    #go to the last node in the lsit
        while current.get_next():
            current = current.get_next()
        current.set_next(Node(data))
    def size(self):
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count-1
    def print_list(self):
        current = self.__head.get_next()
        while current:
            print(current.get_data())
            current = current.get_next()



l = SinglyLinkedList()
l.append('gato')
l.print_list()
l.append("cachorro")
l.append('passalim')

node = l.get_node('passalim')
print(node.get_data())
l.delete('cachorro')
l.print_list()
print(l.size())
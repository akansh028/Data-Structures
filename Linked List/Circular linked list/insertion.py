# Insertion in the doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
    
    def prepend(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next
        print()

    def add_after_node(self,key,data):
        current = self.head
        while current:
            if current.next is None and current.data == key:
                self.append(data)
            elif current.data == key:
                new_node = Node(data)
                nxt = current.next
                current.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            current = current.next

    def add_before_node(self,key,data):
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.prepend(data)
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                prev.next = new_node
                current.prev = new_node
                new_node.next = current
            current = current.next

linked_list = DoublyLinkedList()


linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.append('D')
linked_list.append('E')
linked_list.append('F')
linked_list.print_list()
print('---------------')

linked_list.prepend('Z')
linked_list.print_list()
print('-----------------')

linked_list.add_after_node('A','G')
linked_list.print_list()
print('-------------------')

linked_list.add_before_node('F','H')
linked_list.print_list()
print('-------------------')
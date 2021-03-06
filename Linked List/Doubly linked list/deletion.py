# Deletion in a doubly linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

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
                new_node.next = current
                current.prev = new_node
            current = current.next        

    def deletion(self,key):
        current = self.head
        while current:
            if current.data == key and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            elif current.data == key:
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
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

linked_list.deletion('E')
linked_list.print_list()
print('-----------------')



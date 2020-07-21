# Insertion in the linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data , end=" ")
            current = current.next
        print()
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_in_between(self,prev,data):
        
        if not prev:
            print("No previous node in the list")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

linked_list = LinkedList()

linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.append('D')
linked_list.append('E')
linked_list.print_list()
print('-------------')

linked_list.prepend('Z')
linked_list.print_list()
print('-------------')

linked_list.insert_in_between(linked_list.head.next.next.next,'S')
linked_list.print_list()
print('-------------')

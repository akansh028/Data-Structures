# Deletion of the element in the linked list 

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

    def delete(self,pos):
        current = self.head
        if current and current.data == pos:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != pos:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
        
linked_list = LinkedList()

linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.append('D')
linked_list.append('E')
linked_list.print_list()
print('-------------')

linked_list.delete('C')
linked_list.print_list()
print('-------------')

#linked_list.delete_at_pos(1)
linked_list.print_list()
print('-------------')

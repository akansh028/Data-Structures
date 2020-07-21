# reverse all the list


 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    # printing the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data , end=" ")
            current = current.next
        print()
    # inserting the element at the last of the list
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    # inserting the element at the starting of the list
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # inserting the element at the between of the list
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

    # Finding the length of the list by the iterative method
    def length_iterative(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count
    
    # Finding the length of the list by the recursive method
    def length_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    # swapping two nodes
    def swap_nodes(self,key1,key2):
        current = self.head
        if key1 == key2:
            return
        x,y = None , None
        while current:
            if current.data == key1:
                x = current
            if current.data == key2:
                y = current
            current = current.next
        if x and y:
            x.data, y.data = y.data, x.data
        else:
            return

    def reverse_recursive(self):
        def reverse(current,prev):
            if not current:
                return prev
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            return reverse(current  , prev)
        self.head = reverse(current=self.head , prev=None)


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

print(linked_list.length_iterative())
print(linked_list.length_recursive(linked_list.head))
print('-------------')

linked_list.swap_nodes('B','D')
linked_list.print_list()
print("--------------")

linked_list.reverse_recursive()
linked_list.print_list()
print("-------------")
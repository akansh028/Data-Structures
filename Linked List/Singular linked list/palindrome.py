# palindrome or not

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

    # merging the two lists
    def merge_lists(self, l):

        p = self.head
        q = l.head
        s = None
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not p:
            s.next = p
        return new_head

    # removing duplicates from the llist
    def removing_duplicates(self):
        current = self.head
        prev = None

        dupl_values = dict()

        while current:
            if current.data in dupl_values: # if data is duplicate
                prev.next = current.next
                current = None
            else:
                dupl_values[current.data] = 1   # if data is not duplicate
                prev = current
            current = prev.next

    # return a node 
    def return_node_from_last(self,n):
        length = self.length_iterative()    #length of the list
        current = self.head
        while current:
            if length == n:    # from last
                print(current.data)
                return current
            length -= 1     # decreasing one by one
            current = current.next
        if current is None:
            return

    def count_occurance(self,data):
        count = 0
        current = self.head
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def palindrome(self):
        s = ""
        current = self.head
        while current:
            s += current.data
            current = current.next
        return s == s[::-1]
    

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")
llist.print_list()
print(llist.palindrome())
print('-----------------')

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")
llist_2.print_list()
print(llist_2.palindrome())
print('------------')
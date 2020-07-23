# Binary tree 

# Traversal of the binary tree 
# preorder , inorder , postorder

from stacks import Stack

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
    
    def print_tree(self,type):
        if type == 'preorder':
            return self.preorder_print(tree.root,"")
        elif type == 'inorder':
            return self.inorder_print(tree.root,"")
        elif type == 'postorder':
            return self.postorder_print(tree.root,"")
        else:
            print('type' + str(type) + 'not valid')
    
    def preorder_print(self,start,traversal):
        if start:
            traversal += str(start.data) + " "
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += str(start.data) + " "
            traversal = self.inorder_print(start.right,traversal)
        return traversal

    def postorder_print(self,start,traversal):
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal += str(start.data) + " "
        return traversal    

    def preorder(self,start):
        stack = Stack()
        current = start
        visited = False
        traversal = ""
        while not visited:
            if current is not None:
                traversal += str(current.data) + " "
                stack.push(current.data)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    current = current.right
                else:
                    visited = True
        return traversal

    def inorder(self,start):
        stack = Stack()
        current = start
        visited = False
        traversal = ""

        while not visited:
            if current is not None:
                stack.push(current.data)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    traversal += str(current.data) + ' '
                    current = current.right
                else:
                    visited = True
        return traversal

    def postorder(self,start):
        stack = Stack()
        current = start
        visited = False
        traversal = ""

        while not visited:
            if current is not None:
                stack.push(current.data)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    current = current.right
                    traversal += str(current.data) + " "
                else:
                    visited = True
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print("Preorder :")
print(tree.print_tree("preorder"))
print('--------------------------')

print("Inorder")
print(tree.print_tree("inorder"))
print('--------------------------')

print("Postorder")
print(tree.print_tree("postorder"))
print('--------------------------')

print("Preorder Iterative:")
print(tree.print_tree("preorder_print"))
print('--------------------------')


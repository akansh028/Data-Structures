class deque:
    def __init__(self):
        self.items = []
    
    def add_front(self,item):
        self.items.append(item)

    def add_rear(self,item):
        self.items.insert(0,item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
d = deque()
d.add_front('2')
d.add_front('3')
d.add_front('4')
d.add_front('5')
d.add_front('6')
print(d.items) 

d.add_rear('R')
print(d.items) 

d.remove_front()
print(d.items) 

d.remove_rear()
print(d.items) 

print(d.size()) 

print(d.is_empty())

#d.items = []
#print(d.items)

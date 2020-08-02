# basic items sorting ds to enqueue and dequeue and to get size 

from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
        self.size = 0
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def get_size(self):
        return len(self.items)

q = Queue()
q.enqueue('2')    
q.enqueue('3')    
q.enqueue('5')    
q.enqueue('7')    
q.enqueue('8')    
q.enqueue('0')
print(q.items)
print(q.dequeue())
print(q.get_size())
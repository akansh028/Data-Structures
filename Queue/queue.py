# basic queue sorting ds to enqueue and dequeue and to get size 

from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
        self.size = 0
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.popleft()
    
    def get_size(self):
        return len(self.queue)

q = Queue()
q.enqueue('2')    
q.enqueue('3')    
q.enqueue('5')    
q.enqueue('7')    
q.enqueue('8')    
q.enqueue('0')
print(q.queue)
print(q.dequeue())
print(q.get_size())
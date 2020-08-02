# using the two stacks 
# implement the queue

class queue2stack:
    def __init__(self):
        self.in = []
        self.out = []

    def enqueue(self , item):
        self.in.append(item)

    def dequeue(self):
        if not self.out:
            while self.in:
                self.out.append(self.in.pop())
        return self.out.pop()


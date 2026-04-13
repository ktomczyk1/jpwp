
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

q = Queue()

print(q.is_empty())        # True

q.enqueue(10)
print(q.front())           # 10
print(q.is_empty())        # False
print(q.size())            # 1

q.enqueue(20)
print(q.front())           # 10
print(q.size())            # 2

q.dequeue()
print(q.front())           # 20
print(q.size())            # 1
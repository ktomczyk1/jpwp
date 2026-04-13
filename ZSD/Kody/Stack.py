
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = Stack()

print(s.is_empty())        # True

s.push(10)
print(s.peek())            # 10
print(s.is_empty())        # False

s.push(20)
print(s.peek())            # 20 
print(s.size())            # 2

s.pop()
print(s.peek())            # 10
print(s.size())            # 1
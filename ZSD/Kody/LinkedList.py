
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete_front(self):
        if self.head:
            self.head = self.head.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def is_empty(self):
        return self.head is None
    


ll = LinkedList()
print(ll.is_empty())    # True
ll.print_list()         # None

ll.insert_front(10)
print(ll.is_empty())    # False
ll.print_list()         # 10 -> None

ll.insert_front(20)
ll.insert_back(30)
ll.print_list()         # 20 -> 10 -> 30 -> None

ll.delete_front()
ll.print_list()         # 10 -> 30 -> None
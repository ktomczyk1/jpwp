
class Node:
    def __init__(self, value, color="RED"):
        self.value = value
        self.color = color      # "RED" lub "BLACK"
        self.left = None
        self.right = None
        self.parent = None

def print_tree(node, level=0):
    if node is None:
        print("      " * level + "n (B)")
        return

    # prawe poddrzewo
    print_tree(node.right, level + 1)

    # aktualny węzeł
    color = "R" if node.color == "RED" else "B"
    print("      " * level + f"{node.value}({color})")

    # lewe poddrzewo
    print_tree(node.left, level + 1)

def search(node, value):
    if node is None:
        return None

    if node.value == value:
        return node

    if value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)
    
def get_color(node):        # funkcja pomocnicza
    return "BLACK" if node is None else node.color
    
def left_rotate(root, x):
    y = x.right
    x.right = y.left

    if y.left:
        y.left.parent = x

    y.parent = x.parent

    if x.parent is None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

    return root

def right_rotate(root, y):
    x = y.left
    y.left = x.right

    if x.right:
        x.right.parent = y

    x.parent = y.parent

    if y.parent is None:
        root = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x

    x.right = y
    y.parent = x

    return root

def fix_insert(root, node):
    while node != root and get_color(node.parent) == "RED":
        parent = node.parent
        grandparent = parent.parent

        if parent == grandparent.left:
            uncle = grandparent.right

            if get_color(uncle) == "RED":
                parent.color = "BLACK"
                uncle.color = "BLACK"
                grandparent.color = "RED"
                node = grandparent
            else:
                if node == parent.right:
                    root = left_rotate(root, parent)
                    node = parent
                    parent = node.parent

                root = right_rotate(root, grandparent)
                parent.color = "BLACK"
                grandparent.color = "RED"

        else:
            uncle = grandparent.left

            if get_color(uncle) == "RED":
                parent.color = "BLACK"
                uncle.color = "BLACK"
                grandparent.color = "RED"
                node = grandparent
            else:
                if node == parent.left:
                    root = right_rotate(root, parent)
                    node = parent
                    parent = node.parent

                root = left_rotate(root, grandparent)
                parent.color = "BLACK"
                grandparent.color = "RED"

    root.color = "BLACK"
    return root

def insert(root, value):
    if root is None:
        return Node(value, "BLACK")

    current = root
    parent = None

    while current:
        parent = current
        if value < current.value:
            current = current.left
        else:
            current = current.right

    new_node = Node(value, "RED")
    new_node.parent = parent

    if value < parent.value:
        parent.left = new_node
    else:
        parent.right = new_node

    return fix_insert(root, new_node)


# korzeń - czarny
root = Node(13, "BLACK")

# poziom 1 - czerwone
root.left = Node(8, "RED")
root.left.parent = root

root.right = Node(17, "RED")
root.right.parent = root

# poziom 2 - czarne
root.left.left = Node(1, "BLACK")
root.left.left.parent = root.left

root.left.right = Node(11, "BLACK")
root.left.right.parent = root.left

root.right.left = Node(15, "BLACK")
root.right.left.parent = root.right

root.right.right = Node(25, "BLACK")
root.right.right.parent = root.right

# poziom 3 - czerwone
root.left.left.right = Node(6, "RED")
root.left.left.right.parent = root.left.left

root.right.right.left = Node(22, "RED")
root.right.right.left.parent = root.right.right

root.right.right.right = Node(27, "RED")
root.right.right.right.parent = root.right.right



print_tree(root)
print("\n")

print(search(root, 123))             # None
print(search(root, 22))              # <__main__.Node object at 0x000002537D7A7990>  
print(search(root, 22).value)        # 22
print(search(root, 22).color)        # RED
print("\n")

insert(root, 18)
print_tree(root)
print("\n")


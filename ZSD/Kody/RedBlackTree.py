
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
    
def left_rotate(x):
    if x.right is None:
        return
    
    y = x.right
    x.right = y.left

    if y.left:
        y.left.parent = x

    y.parent = x.parent

    if x.parent is None:
        global root
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

def right_rotate(y):
    if y.left is None:
        return
    
    x = y.left
    y.left = x.right

    if x.right:
        x.right.parent = y

    x.parent = y.parent

    if y.parent is None:
        global root
        root = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x

    x.right = y
    y.parent = x

def fix_insert(node):
    while node != root and get_color(node.parent) == "RED":
        parent = node.parent
        grandparent = parent.parent

        if parent == grandparent.left:
            uncle = grandparent.right

            # uncle RED → recoloring
            if get_color(uncle) == "RED":
                parent.color = "BLACK"
                uncle.color = "BLACK"
                grandparent.color = "RED"
                node = grandparent

            else:
                # Left-Right
                if node == parent.right:
                    left_rotate(parent)
                    node = parent
                    parent = node.parent

                # Left-Left
                right_rotate(grandparent)
                parent.color = "BLACK"
                grandparent.color = "RED"

        else:
            uncle = grandparent.left

            # CASE 1 (mirror)
            if get_color(uncle) == "RED":
                parent.color = "BLACK"
                uncle.color = "BLACK"
                grandparent.color = "RED"
                node = grandparent

            else:
                # CASE 2: Right-Left
                if node == parent.left:
                    right_rotate(parent)
                    node = parent
                    parent = node.parent

                # CASE 3: Right-Right
                left_rotate(grandparent)
                parent.color = "BLACK"
                grandparent.color = "RED"

    root.color = "BLACK"

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

    fix_insert(new_node)
    return root


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


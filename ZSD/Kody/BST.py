
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def print_tree(node, level=0):
    if node is None:
        print("      " * level)
        return

    # prawe poddrzewo
    print_tree(node.right, level + 1)

    # aktualny węzeł
    print("      " * level + f"{node.value}")

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


# budowa drzewa
root = Node(4)

root.left = Node(2)
root.left.parent = root

root.right = Node(6)
root.right.parent = root

root.left.left = Node(1)
root.left.left.parent = root.left

root.left.right = Node(3)
root.left.right.parent = root.left

root.right.left = Node(5)
root.right.left.parent = root.right

root.right.right = Node(7)
root.right.right.parent = root.right

print_tree(root)
print("\n")
root = right_rotate(root, root)
print_tree(root)
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def isBalanced(root):
    if root is None:
        return True


    lHeight = height(root.left)
    rHeight = height(root.right)

    if abs(lHeight - rHeight) > 1:
        return False


    return isBalanced(root.left) and isBalanced(root.right)


if __name__ == "__main__":

    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)

    print("true" if isBalanced(root) else "false")
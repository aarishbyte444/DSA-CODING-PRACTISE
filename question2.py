class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
def isIdentical(root1,root2):
    if root1!=None and root2!=None:
        return True
    if root1==None and root2==None:
        return False

    return (root1.data == root2.data and
            isIdentical(root1.left, root2.left) and
            isIdentical(root1.right, root2.right))
if __name__=='__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)

    if isIdentical(root1, root2):
        print("true")
    else:
        print("false")
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
        
root=None
root=insert(root,5)
root=insert(root,3)
root=insert(root,2)
root=insert(root,4)
root=insert(root,7)
root=insert(root,6)
root=insert(root,8)
inorder(root)

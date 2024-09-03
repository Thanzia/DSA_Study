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

def search(node, x):
        if node is None:
            return False
        if node.data==x:
            return True
        elif node.data<x:
            return search(node.right,x)
        else:
            return search(node.left,x)
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

#pbm 1:convert BT to BST

def storeInorder(self,root, inorder):
        # Base Case
        if root is None:
            return
        # First store the left subtree
        self.storeInorder(root.left, inorder)
    
        # Copy the root's data
        inorder.append(root.data)

        # Finally store the right subtree
        self.storeInorder(root.right, inorder)

    # A helper function to count nodes in a binary tree
    def countNodes(self,root):
        if root is None:
            return 0

        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    # Helper function that copies contents of sorted array 
    # to Binary tree
    def arrayToBST(self,arr, root):
        # Base Case
        if root is None:
            return
    
        # First update the left subtree
        self.arrayToBST(arr, root.left)

        # now update root's data delete the value from array
        root.data = arr[0]
        arr.pop(0)

        # Finally update the right subtree
        self.arrayToBST(arr, root.right)

    # This function converts a given binary tree to BST
    def binaryTreeToBST(self,root):
        # Base Case: Tree is empty
        if root is None:
            return
    
        # Count the number of nodes in Binary Tree so that 
        # we know the size of temporary array to be created
        n = self.countNodes(root)

        # Create the temp array and store the inorder traversal 
        # of tree 
        arr = []
        self.storeInorder(root, arr)
    
        # Sort the array
        arr.sort()

        # copy array elements back to binary tree
        self.arrayToBST(arr, root)
        
root=None
root=insert(root,5)
root=insert(root,3)
root=insert(root,2)
root=insert(root,4)
root=insert(root,7)
root=insert(root,6)
root=insert(root,8)
inorder(root)

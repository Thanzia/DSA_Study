#Binary Tree
#create a node first and then branches to
#left and right and hence create left and right nodes

class Node:
    def __init__ (self , data):
        self.data = data
        self.left = None
        self.right = None

        
#TRAVERSING thru the binary tree

#create class binary tree        
class Binary_Tree:

    #preorder traversal like  t.c:O(n),s.c:O(1)or O(h)
    #root->left->right
    
    def __preorder__(self, root):
        
        if root is None:
            return
        print(root.data)
        self.__preorder__(root.left)
        self.__preorder__(root.right)
        
    #inorder traversal like t.c :O(n) s.c:O(1)or O(h)
    #left->root->right
        
    def __inorder__(self , root):
        if root is None:
            return
        self.__inorder__(root.left)
        print(root.data)
        self.__inorder__(root.right)

    #postorder traversal like
    #left->right->root
        
    def __postorder__(self, root):
        if root is None:
            return
        self.__postorder__(root.left)
        self.__postorder__(root.right)
        print(root.data)

#level order traversing
        
    def printLevelOrder(self,root):
        if root is None:
            return

        # Create an empty queue
        queue = []

        # Enqueue Root and initialize height
        queue.append(root)
        #print(queue)

        while(len(queue) > 0):
            # Print front of queue and
            # remove it from queue
            print(queue[0].data, end=" ")
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

        print()

#to find the height of the tree  t.c:O(n),s.c:O(n)
        
        def maxdepth(self,root):
        if root is None:
            return 0
        else:
            ldepth=self.maxdepth(root.left)
            rdepth=self.maxdepth(root.right)

            #uselarger one
            if(ldepth>rdepth):
                return ldepth+1
            else:
                return rdepth+1

#INSERTION
#function to insert element in binary tree
#t.c:O(v),v no.of nodes   s.c:O(B) B width of tree
            
    def insert(self,root,key):
        if not root:
            root = newNode(key)
            return
        q = []
        q.append(root)
        # Do level order traversal until we find
        # an empty place.
        while (len(q)):
            root = q[0]
            q.pop(0)

            if (not root.left):
                root.left = newNode(key)
                break
            else:
                q.append(root.left)
            if (not root.right):
                root.right = newNode(key)
                break
            else:
                q.append(root.right)


#DELETION 
#algo:Starting at the root, find the deepest and rightmost node in the tree
#and the node which we want to delete. 
#Replace the deepest rightmost node’s data with the node to be deleted. 
#Then delete the deepest rightmost node.
                
# function to delete the given deepest node (d_node) in binary tree
def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
 


#function to delete element in binary tree

def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        key_node.data = x
        deleteDeepest(root, temp)
    return root


#create a binary tree
root = Node("A")
root.left = Node("B")
root.right = Node ("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

btree = Binary_Tree()
#btree.__preorder__(root)
#btree.__postorder__(root)
#btree.__inorder__(root)
btree.printLevelOrder(root)
btree.insert(root,"T")

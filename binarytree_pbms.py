
#pbm 1: B.T zigzag level order traversal

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # List to store the result of zigzag traversal
        result = []
        
        # Check if the root is None, return an empty result
        if not root:
            return result
        
        # Queue to perform level order traversal
        nodesQueue = deque()
        nodesQueue.append(root)
        
        # Flag to determine the direction of traversal (left to right or right to left)
        leftToRight = True
        
        # Continue traversal until the queue is empty
        while nodesQueue:
            # Get the number of nodes at the current level
            size = len(nodesQueue)
            
            # List to store the values of nodes at the current level
            row = [0] * size
            
            # Traverse nodes at the current level
            for i in range(size):
                # Get the front node from the queue
                node = nodesQueue.popleft()
                
                # Determine the index to insert the node's value based on the traversal direction
                index = i if leftToRight else (size - 1 - i)
                
                # Insert the node's value at the determined index
                row[index] = node.val
                
                # Enqueue the left and right children if they exist
                if node.left:
                    nodesQueue.append(node.left)
                if node.right:
                    nodesQueue.append(node.right)
            
            # Switch the traversal direction for the next level
            leftToRight = not leftToRight
            
            # Add the current level's values to the result list
            result.append(row)
        
        # Return the final result of zigzag level order traversal
        return result
    
#pbm 2: Bottom view of Binar Tree

from queue import Queue
class Solution:
    def bottomView(self, root):
        """#Function to return the
        bottom view of the binary tree
        """
        # Vector to store the result
        ans = []

        # Check if the tree is empty
        if root is None:
            return ans

        # Map to store the bottom view nodes
        # based on their vertical positions
        mpp = defaultdict(int)

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical position
        q = Queue()

        # Push the root node with its vertical
        # position (0) into the queue
        q.put((root, 0))

        # BFS traversal
        while not q.empty():
            # Retrieve the node and its vertical
            # position from the front of the queue
            it = q.get()
            node, line = it[0], it[1]

            # Update the map with the node's data
            # for the current vertical position
            mpp[line] = node.data

            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.put((node.left, line - 1))

            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.put((node.right, line + 1))

        # Transfer values from the
        # map to the result vector
        for key, value in sorted(mpp.items()):
            ans.append(value)

        return ans

#pbm 3: Top view of B.T

from collections import deque
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # Vector to store the result
        ans = []
        
        # Check if the tree is empty
        if not root:
            return ans
        
        # Map to store the top view nodes
        # based on their vertical positions
        mpp = {}
        
        # Queue for BFS traversal, each element
        # is a pair containing node 
        # and its vertical position
        q = deque([(root, 0)])
        
        # Push the root node with its vertical
        # position (0) into the queue
        while q:
            # Retrieve the node and its vertical
            # position from the front of the queue
            node, line = q.popleft()
            
            # If the vertical position is not already
            # in the map, add the node's data to the map
            if line not in mpp:
                mpp[line] = node.data
            
            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.append((node.left, line - 1))
            
            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.append((node.right, line + 1))
        
        # Transfer values from the
        # map to the result vector
        for value in sorted(mpp.items()):
            ans.append(value[1])
        
        return ans

#pbm 4: find maximum path sum

class Solution:
    def findMaxPathSum(self, root, maxi):
        # Recursive function to find the maximum path sum
        # for a given subtree rooted at 'root'
        # The variable 'maxi' is a reference parameter
        # updated to store the maximum path sum encountered

        # Base case: If the current node is None, return 0
        if root is None:
            return 0

        # Calculate the maximum path sum
        # for the left and right subtrees
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))

        # Update the overall maximum
        # path sum including the current node
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.val)

        # Return the maximum sum considering
        # only one branch (either left or right)
        # along with the current node
        return max(leftMaxPath, rightMaxPath) + root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Function to find the maximum
        # path sum for the entire binary tree

        # Initialize maxi to the
        # minimum possible integer value
        maxi = [float('-inf')] 
        # Call the recursive function to
        # find the maximum path sum
        self.findMaxPathSum(root, maxi)
        # Return the final maximum path sum
        return maxi[0]


#pbm 5: construct B.T from inorder and postorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Function to build a binary tree
        from inorder and postorder traversals
        """
        if len(inorder) != len(postorder):
            return None

        # Create a map to store the indices
        # of elements in the inorder traversal
        hm = {val: i for i, val in enumerate(inorder)}

        # Call the recursive function
        # to build the binary tree
        return self.buildTreePostIn(inorder, 0, len(inorder) - 1, postorder, 0,
                                     len(postorder) - 1, hm)

        #ps:postorder starting index initially 0
        #is:inorder starting index   0
        #pe:ending index n-1
        #ie:ending index  n-1
 
    def buildTreePostIn(self, inorder: List[int], is_, ie, postorder: List[int], ps, pe, hm):
        """
        Recursive function to build a binary
        tree from inorder and postorder traversals
        """
        # Base case: If the subtree
        # is empty, return None
        if ps > pe or is_ > ie:
            return None

        # Create a new TreeNode
        # with the root value from postorder
        root = TreeNode(postorder[pe])

        # Find the index of the root
        # value in inorder traversal
        inRoot = hm[postorder[pe]]

        # Number of nodes in the left subtree
        numsLeft = inRoot - is_

        # Recursively build the
        # left and right subtrees
        root.left = self.buildTreePostIn(inorder, is_, inRoot - 1, postorder,
                                         ps, ps + numsLeft - 1, hm)

        root.right = self.buildTreePostIn(inorder, inRoot + 1, ie, postorder,
                                          ps + numsLeft, pe - 1, hm)

        # Return the root of
        # the constructed subtree
        return root

#pbm 6: LCA of B.T

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None  or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left==None:
            return right
        elif right==None:
            return left
        else:
            return root

#pbm 7: Vertical order traversal of B.T

from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = defaultdict(lambda: defaultdict(lambda: list()))
        todo = deque([(root, (0, 0))])

        while todo:
            temp, (x, y) = todo.popleft()
            nodes[x][y].append(temp.val)

            if temp.left:
                todo.append((temp.left, (x - 1, y + 1)))

            if temp.right:
                todo.append((temp.right, (x + 1, y + 1)))

        ans = []
        for x, y_vals in sorted(nodes.items()):
            col = []
            for y, values in sorted(y_vals.items()):
                col.extend(sorted(values))
            ans.append(col)
        
        return ans





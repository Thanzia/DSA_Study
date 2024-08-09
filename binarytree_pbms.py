
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


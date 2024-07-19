# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import itertools
class Solution:

    def find_lca_dfs(self,root, n1, n2):
        if not root:
            return None
        
        if root.val == n1 or root.val == n2:
            return root

        left_lca = self.find_lca_dfs(root.left, n1, n2)
        right_lca = self.find_lca_dfs(root.right, n1, n2)

        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca
    
    def find_distance_dfs(self,root, target, dist):
        if not root:
            return -1

        if root.val == target:
            return dist

        left_dist = self.find_distance_dfs(root.left, target, dist + 1)
        if left_dist != -1:
            return left_dist

        return self.find_distance_dfs(root.right, target, dist + 1)
    
    def find_leaves(self,node,leaves):
        if not node:
            return 

        if not node.left and not node.right:
            leaves.append(node.val)
        self.find_leaves(node.left,leaves)
        self.find_leaves(node.right,leaves)
        return leaves
        

    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0
        count_pairs=0
        leaves=[]
        
        leaves=self.find_leaves(root,leaves)
        
        for n1, n2 in itertools.combinations(leaves, 2):
            lca = self.find_lca_dfs(root, n1, n2)
            if not lca:
                continue
            distance_n1 = self.find_distance_dfs(lca, n1, 0)
            distance_n2 = self.find_distance_dfs(lca, n2, 0)
            total_distance= distance_n1 + distance_n2
            if(total_distance)<=distance:
                count_pairs+=1
            
        return count_pairs

    

def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp=None
        if arr[i] is not None:
            temp = TreeNode(arr[i])
            root = temp
            root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
            root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root        

nums=[80,62,99,36,45,39,76,81,44,23,58,8,14,1,94,100,10,8,30,75,7,33,80,44,2,67,78,64,30,98,100,24,48,42,31,91,37,81,45,30,77,28]
distance = 8

root = None
root = insertLevelOrder(nums, root, 0, len(nums))

sol = Solution()
result = sol.countPairs(root, distance)
print("Number of good leaf node pairs:", result)
        
        






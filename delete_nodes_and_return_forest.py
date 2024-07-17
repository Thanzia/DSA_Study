# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional, Set
from collections import deque
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []
    
        def helper(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None
            to_delete = node.val in to_delete_set
            if is_root and not to_delete:
                forest.append(node)
            node.left = helper(node.left, to_delete)
            node.right = helper(node.right, to_delete)
            return None if to_delete else node
    
        helper(root, True)
        return forest


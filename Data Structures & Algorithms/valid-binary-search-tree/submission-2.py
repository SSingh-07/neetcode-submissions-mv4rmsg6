# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalidnode(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (isvalidnode(node.left, left, node.val) 
                    and isvalidnode(node.right, node.val, right))

        return isvalidnode(root, float("-inf"), float("inf"))
        
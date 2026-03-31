# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])

        if not root:return root

        while queue:
            child = queue.popleft()
            child.left, child.right = child.right, child.left

            if child.left:
                queue.append(child.left)

            if child.right:
                queue.append(child.right)

        return root
        
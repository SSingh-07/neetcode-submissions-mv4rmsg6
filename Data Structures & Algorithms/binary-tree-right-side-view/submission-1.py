# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rightcheck(root):
            queue = deque([root])

            while queue:
                length = len(queue)
                value = None

                for i in range(length):
                    node = queue.popleft()

                    if node:
                        value = node.val
                        queue.append(node.left)
                        queue.append(node.right)
                        
                if value!= None:
                    res.append(value)


        rightcheck(root)
        return res
        
        
        
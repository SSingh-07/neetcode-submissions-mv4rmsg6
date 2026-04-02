# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque([root])
        visited = []

        while d:
            length = len(d)
            temp = []

            for i in range(length):
                node = d.popleft()

                if node:
                    temp.append(node.val)
                    d.append(node.left)
                    d.append(node.right)

            if temp:
                visited.append(temp)

        return visited
        
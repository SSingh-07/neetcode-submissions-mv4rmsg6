class Solution:


    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        length = len(nums)
        stack = []

        def sbset(i):
            if i == length:
                return 0
            stack.append(nums[i])
            res.append(stack.copy())
            sbset(i+1)
            stack.pop()
            sbset(i+1)

        sbset(0)
        res.append([])

        return res




        
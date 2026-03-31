class Solution:


    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        length = len(nums)
        stack = []

        def sbset(i):
            if i == length:
                res.append(stack.copy())
                return 0

            stack.append(nums[i])
            sbset(i+1)
            stack.pop()
            sbset(i+1)

        sbset(0)

        return res




        
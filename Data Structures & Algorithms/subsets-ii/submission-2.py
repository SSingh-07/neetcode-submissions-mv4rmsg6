class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        nums.sort()
        stack = []

        def sbset(i):
            if i == length:
                res.append(stack.copy())
                return 0

            stack.append(nums[i])
            sbset(i+1)
            stack.pop()

            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            sbset(i+1)

        sbset(0)
        # res.append([])

        return res

        

        
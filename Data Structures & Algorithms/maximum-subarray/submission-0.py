class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = nums[0], 0

        for i in nums:
            if curr < 0:
                curr = 0
            curr+=i
            res = max(res, curr)

        return res
        
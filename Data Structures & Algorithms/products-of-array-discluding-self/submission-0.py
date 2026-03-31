class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod =1
        rightprod = 1
        result = [1]*len(nums)

        for i, j in enumerate(nums):
            result[i] = leftprod
            leftprod*=j

        for i, j in enumerate(nums[::-1]):
            result[-1-i] *= rightprod
            rightprod*=j

        return result

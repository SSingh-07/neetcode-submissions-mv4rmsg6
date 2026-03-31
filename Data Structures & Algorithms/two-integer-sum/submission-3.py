class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i, j in enumerate(nums):
            if (target- j) in check:
                return sorted([check[(target-j)], i])

            check[j]=i
        


        
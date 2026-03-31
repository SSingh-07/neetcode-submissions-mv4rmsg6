class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        rit = len(nums) - 1
        if rit == 2:
            if sum(nums) == 0:
                return[nums]
            else:
                return []

        for (i,val) in enumerate(nums):
            if i > 0 and val == nums[i -1]:
                continue

            left, right = i + 1, rit
            while left < right:
                summ = val + nums[left] + nums[right]
                if summ < 0:
                    left += 1
                elif summ > 0:
                    right -= 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left +=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return res
        
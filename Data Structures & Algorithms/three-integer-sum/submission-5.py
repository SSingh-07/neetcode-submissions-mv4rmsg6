class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)-1
        if length+1< 3:
            return []

        nums.sort()
        res = []

        for i,a in enumerate(nums):

            if a>0 :
                break
            if i>0 and nums[i-1]==a:
                continue
            l=i+1
            r = length 

            while l<r:
                if a + nums[l] + nums[r] > 0:
                    r-=1
                elif a + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return res

        
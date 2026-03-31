class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if r == 0:
            return nums[-1]
        if nums[l] < nums[r]:
            return nums[l]

        while l<=r:
            mid = (r + l)//2
            # print(mid)
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] <= nums[-1]:
                r = mid -1
            elif nums[mid] > nums[-1]:
                l = mid+1
        
        return nums[mid]

        
            
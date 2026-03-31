class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if r == 0:
            return -1 if nums[-1]!=target else 0

        while l<=r:
            mid = (l + r)//2
            # print(mid)
            if nums[mid] == target:
                return mid

            # if mid is in the left sorted area
            if nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l]> target:
                    l = mid +  1
                else:
                    r = mid-1

            # if mid is in the right sorted area
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid -1
                else:
                    l = mid + 1

        return -1
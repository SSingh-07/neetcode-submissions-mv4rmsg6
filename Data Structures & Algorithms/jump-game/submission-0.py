class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        goal = last

        for i in range(last, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
        
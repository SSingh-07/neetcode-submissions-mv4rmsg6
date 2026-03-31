class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for j,i in enumerate(nums):
            if (target - i) in visited:
                return [visited[target - i], j]
            else:
                visited[i] = j

        
            


                
        
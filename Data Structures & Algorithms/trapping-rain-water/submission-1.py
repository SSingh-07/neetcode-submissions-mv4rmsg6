class Solution:
    def trap(self, height: List[int]) -> int:
        l, leftmax = 0, height[0]
        r , rightmax = len(height) - 1, height[-1]
        vol = 0

        while l < r:
            if leftmax < rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                vol+= leftmax - height[l]
            elif leftmax > rightmax:
                r-=1
                rightmax = max(rightmax, height[r])
                vol+=rightmax - height[r]

            else:
                l+=1
                leftmax = max(leftmax, height[l])
                vol+= leftmax - height[l]
        return vol
        
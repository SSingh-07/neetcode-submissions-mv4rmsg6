class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i,j in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] >= j:
                stack.append(i)

            else:
                while stack and temperatures[stack[-1]] <j:
                    curr = stack.pop()
                    result[curr] = i-curr
                stack.append(i)
            # print(stack)
        
        return result

        
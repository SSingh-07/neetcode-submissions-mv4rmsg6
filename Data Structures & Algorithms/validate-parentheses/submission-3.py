class Solution:
    def isValid(self, s: str) -> bool:
        opens = set(['(', '{', '['])
        pairs = {'(':')', '{':'}', '[':']'}
        stack =[]

        for i in s:
            if i in opens:
                stack.append(i)
            else:
                if not stack:
                    return False
                if pairs[stack[-1]]!=i:
                    return False
                stack.pop()

        return True if not stack else False

        
class Solution:
    def isValid(self, s: str) -> bool:
        check =[]
        
        for i in s:
            if i in {'(','{','['}:
                check.append(i)
            elif check:
                if i == ')' and check[-1] == '(':
                    check.pop()
                elif i == '}' and check[-1] == '{':
                    check.pop()

                elif i == ']' and check[-1] == '[':
                    check.pop()
                else:
                    return False
            else:
                return False

        return len(check) == 0
            


        
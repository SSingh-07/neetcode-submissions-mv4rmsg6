class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        if len(tokens) ==1:
            return tokens[-1]

        for i in tokens:
            res.append(i)
            
            if res[-1] == '+':
                res[-3] = int(res[-3]) + int(res[-2])
                res.pop()
                res.pop()

            elif res[-1] == '-':
                res[-3] = int(res[-3]) - int(res[-2])
                res.pop()
                res.pop()                

            elif res[-1] == '*':
                res[-3] = int(res[-3]) * int(res[-2])
                res.pop()
                res.pop()
                
            elif res[-1] == '/':
                res[-3] = int(int(res[-3])/int(res[-2]))
                res.pop()
                res.pop()

            
                    

        return res[0]

                


        
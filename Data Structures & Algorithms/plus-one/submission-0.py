class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        
        carry = (digits[-1] + 1)//10
        digits[-1] = (digits[-1] + 1)%10
        track = 1
        while carry and abs(-1-track) <=length:
            carry = (digits[-1-track] + 1)//10
            digits[-1-track] = (digits[-1-track] + 1)%10
            track+=1
        
        if carry:
            digits.insert(0,1)

        return digits

        

        
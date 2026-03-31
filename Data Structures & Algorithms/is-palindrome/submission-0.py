class Solution:
    def isPalindrome(self, s: str) -> bool:

        data = []
        for i in s:
            if i.isalnum():
                data.append(i.lower())

        return data == data[::-1]       
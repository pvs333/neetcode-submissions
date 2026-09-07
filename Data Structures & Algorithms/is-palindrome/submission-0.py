class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr+=c.lower()

        l = list(newStr)
        k = l[::-1]
        print(l)
        print(k)
        if l==k:
            return True
        else:
            return False
        
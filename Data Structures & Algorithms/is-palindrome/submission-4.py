class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        for i in range(0,n//2):
            if s[i]!=s[n-1-i]:
                return False
        return True


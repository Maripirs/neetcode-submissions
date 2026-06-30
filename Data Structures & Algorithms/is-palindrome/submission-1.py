class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0;
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char.lower()
        r = len(newS) -1

        while  l < r:

            if newS[l] != newS[r]:
                return False
            l = l+1
            r = r-1
            
        return True
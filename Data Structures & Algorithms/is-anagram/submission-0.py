class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if (len(s) != len(t)):
            return False
        for char in s:
            if char in letters:
                letters[char]+= 1
            else:
                letters[char] = 1

        for char in t:
            if char in letters and letters[char]:
                letters[char] -= 1
            else:
                return False
        return True
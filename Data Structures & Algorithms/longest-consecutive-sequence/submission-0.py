class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in numset:
            if num-1 not in numset:
                length = 0
                value = num
                while value in numset:
                    length += 1
                    value += 1
                if length > longest:
                    longest = length
        return longest

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for string in strs:
            srted = "".join(sorted(string))
            if srted in grouped:
                grouped[srted].append(string)
            else:
                grouped[srted] = [string]
        return list(grouped.values())
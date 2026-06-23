class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        srted = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for i,item in enumerate(sorted(counts.items(), key = lambda item: item[1], reverse = True)):
            srted.append(item[0])
            if i == k-1:
                break
        return srted


            
                
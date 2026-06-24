class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pref = [1]
        suf = [1]
        for i, num in enumerate(nums):
            # print(f"suf {suf}, nums[-i-1] {nums[-i-1]}")
            pref.append( pref[i] * num)
            suf.append(suf[i] * nums[-i-1])




        for i, num in enumerate(nums):
            # print(pref[i], " * " ,suf[-2-i])
            output.append(pref[i] * suf[-i-2])
        print (pref)
        print (suf)
        return output


        
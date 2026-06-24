class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i, string in enumerate(strs):
            encoded += f"#{len(string)}#" + string

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 1
        decoded = []
        length = ""

        print(s)
        while i < len(s):
            print(i, s[i])
            if s[i] == "#":
                print ("i = ", i, ", length = ", length )
                decoded.append(s[i+1:i+int(length)+1])
                i = i + int(length) + 2
                length = ""
                print("i skip to", i)
            else:
                print("Adding to length " + s[i])
                length = length + s[i]
                i = i+1

            
        return decoded
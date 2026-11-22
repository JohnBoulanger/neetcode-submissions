class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "@" + s for s in strs)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # determine how many digits the number is
            start = i
            while s[i] != "@":
                i += 1
            
            # extract the length
            length = int(s[start : i])
            i += 1
            # extract the string after the delimiter of length l
            result.append(s[i : i + length])
            i += length

        return result

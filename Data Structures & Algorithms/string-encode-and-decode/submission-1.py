class Solution:

    # use length of each string and append it to the start of the word so we know
    # how long that word is
    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(string)) + "@" + string for string in strs])
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find separator
            j = i
            while s[j] != "@":
                j += 1

            dist = j - i + 1

            length = int(s[i:j])
            result.append(s[(i + dist):(i + length + dist)])
            i += length + dist

        return result

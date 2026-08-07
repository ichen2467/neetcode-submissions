class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s) and s[i].isdigit():
            count = int(s[i])
            i += 1
            while s[i].isdigit():
                count *= 10
                count += int(s[i])
                i += 1
            i += 1
            decoded_strs.append("")
            while count > 0:
                decoded_strs[-1] += s[i]
                i += 1
                count -= 1
        return decoded_strs
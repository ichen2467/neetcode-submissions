class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        return "".join(parts)

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
            decoded_strs.append(s[i:i + count])
            i += count
        return decoded_strs
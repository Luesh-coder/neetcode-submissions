class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for x in range(n + 1):
            res.append(bin(x).count('1'))
        return res
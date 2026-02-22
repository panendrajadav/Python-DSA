class Solution:
    def binaryGap(self, n: int) -> int:
        s=bin(n)[2:]
        l=-1
        max_gap=0
        for i in range(len(s)):
            if s[i]=='1':
                if l !=-1:
                    max_gap=max(max_gap,i-l)
                l=i
        return max_gap
        
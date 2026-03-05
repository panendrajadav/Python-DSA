class Solution:
    def minOperations(self, s: str) -> int:
        c1=c2=0
        for i in range(len(s)):
            bit=int(s[i])
            c1+=bit^i%2
            c2+=bit^(1-(i%2))
        return(min(c1,c2))
        
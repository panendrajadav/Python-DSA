class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen=set()
        for i in range(len(s)-k+1):
            seen.add(s[i:k+i])
        return len(seen)==2**k

        
            
        
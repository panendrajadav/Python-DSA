class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        org =x
        res=0
        while x>0:
            last = x%10
            res=res*10+last
            x//=10
            
        return org== res

            
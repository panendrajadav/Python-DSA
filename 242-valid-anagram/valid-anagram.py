class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ch={}
        for i in s:
            ch[i] = ch.get(i,0)+1
        for i in t:
            if i not in ch:
                return False
            ch[i]-=1
            if ch[i]<0:
                return False
        return True


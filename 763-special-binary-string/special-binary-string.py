class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        start=0
        count=0
        sub=[]
        for i in range(len(s)):
            if s[i]=='1':
                count+=1
            else:
                count-=1

            if count==0:
                inner=self.makeLargestSpecial(s[start+1:i])
                sub.append("1"+inner+"0")
                start=i+1
            sub.sort(reverse=True)
        return "".join(sub)    
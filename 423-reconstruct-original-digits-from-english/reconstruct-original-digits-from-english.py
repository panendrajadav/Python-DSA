class Solution:
    def originalDigits(self, s: str) -> str:
        from collections import Counter
        c=[0]*10
        freq = Counter(s)
        c[0]=freq['z']
        c[2]=freq['w']
        c[4]=freq['u']
        c[6]=freq['x']
        c[8]=freq['g']
        c[1]= freq['o']-c[0]-c[2]-c[4]
        c[3]=freq['h']-c[8]
        c[5]=freq['f']-c[4]
        c[7]=freq['s']-c[6]
        c[9]= freq['i']-c[5]-c[6]-c[8]

        res=[]
        for i in range(10):
            res.append(str(i) * c[i])
        return "".join(res)
        
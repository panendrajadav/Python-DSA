class Solution:
    def uniqueOccurrences(self, arr):
        mp = {}
        for i in arr:
            mp[i] = mp.get(i,0) + 1
        s = set()
        for count in mp.values():
            if count in s:
                return False
            s.add(count)
        return True
# Permutation in String - https://leetcode.com/problems/permutation-in-string/
# Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def charactersMap(self, s1: str) -> dict[str, int]:
        s1charactersmap = {}
        for i in s1:
            occ_i = s1charactersmap.get(i, 0)
            occ_i+=1
            s1charactersmap[i]=occ_i
        return s1charactersmap
    def compareDict(self, d1: dict[str, int], d2: dict[str, int]) -> bool:
        for i in d1:
            if not(d2.get(i)) or d2.get(i) != d1[i]:
                return bool(False)
        for i in d2:
            if not(d1.get(i)) or d1.get(i) != d2[i]:
                return bool(False)
        return bool(True)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1charactersmap = self.charactersMap(s1)
        l = len(s1)
        i = 0
        j = l-1
        #print(s1charactersmap)
        #return bool(False)
        while(j < len(s2)):
            windowCharactersMap = self.charactersMap(s2[i:(j+1)])
            #print(i,j, s2[i:j], windowCharactersMap, s1charactersmap)
            if self.compareDict(windowCharactersMap, s1charactersmap):
                return bool(True)
            i+=1
            j+=1
        return bool(False)

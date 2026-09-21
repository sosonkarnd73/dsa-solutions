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

#sol 2
class Solution:
    def charactersMap(self, s1: str) -> dict[str, int]:
        s1charactersmap = {}
        for i in s1:
            occ_i = s1charactersmap.get(i, 0)
            occ_i+=1
            s1charactersmap[i]=occ_i
        return s1charactersmap
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1charactersmap = self.charactersMap(s1)
        l = len(s1)
        i = 0
        j = 0
        windowCharactersMap = {}
        while(j < len(s2)):
            c = s2[j]
            
            count_c = windowCharactersMap.get(c, 0) + 1
            windowCharactersMap[c]=count_c
            count_c_s1 = s1charactersmap.get(c)
            if not(count_c_s1):
                windowCharactersMap = {}
                i = j+1
                j = j+1
            elif count_c > count_c_s1:
                while count_c > count_c_s1:
                    windowCharactersMap[s2[i]] = windowCharactersMap[s2[i]] - 1
                    if s2[i] == c:
                        count_c-=1
                    i+=1
                j = j+1
            elif count_c == count_c_s1 and (j - i +1) == l:
                return bool(True)
            else:
                j+=1
        return bool(False)

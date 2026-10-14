# Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def charactersMap(self, s1: str) -> dict[str, int]:
        s1charactersmap = {}
        for i in s1:
            occ_i = s1charactersmap.get(i, 0)
            occ_i+=1
            s1charactersmap[i]=occ_i
        return s1charactersmap
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        tcharactersmap = self.charactersMap(t)
        required = len(tcharactersmap)
        i = 0
        j = 0
        sol_l = None
        sol_r = None
        found = 0
        windowCharactersMap = {}
        while(j < m):
            char = s[j]
            windowCharactersMap[char] = windowCharactersMap.get(char, 0) + 1

            count_char_t = tcharactersmap.get(char, 0)
            if count_char_t and count_char_t == windowCharactersMap[char]:
                found+=1
            while(i <= j and found == required):
                char_l = s[i]
                #print(found, i, j, sol_l, sol_r, windowCharactersMap)
                if (sol_r == None and sol_l == None) or (j - i < sol_r - sol_l):
                    sol_r = j
                    sol_l = i
                windowCharactersMap[char_l] -= 1 
                if tcharactersmap.get(char_l) and tcharactersmap[char_l] > windowCharactersMap[char_l]:
                    found-=1
                i += 1
            j+=1
        if sol_r == None:
            return ""
        else:
            return s[sol_l:sol_r+1]

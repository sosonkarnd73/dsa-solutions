# Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subarray = [-1] * 255
        l = len(s)
        i = 0
        max_len = 0
        k = -1
        curr_subarray_length = 0
        for j in range(0, l):
            k = subarray[ord(s[j])]
            curr_subarray_length = j - i
            if k != -1:
                if curr_subarray_length >= max_len:
                    max_len = curr_subarray_length
                while i <= k:
                    kk = ord(s[i])
                    subarray[kk] = -1
                    i += 1
            subarray[ord(s[j])] = j
        if k == -1:
            curr_subarray_length = l - i
            if curr_subarray_length > max_len:
                max_len = curr_subarray_length
        return max_len

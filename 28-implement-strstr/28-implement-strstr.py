class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if len(needle)==len(haystack):
            if needle==haystack:
                return 0
            else:
                return -1
        for i in range((len(haystack)-len(needle))+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
            
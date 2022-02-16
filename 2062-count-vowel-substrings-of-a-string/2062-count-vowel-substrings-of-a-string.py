class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        x=['a','e','i','o','u']
        ans=0
        for i in range(len(word)):
            for j in range(i+1,len(word)):
                if set(word[i:j+1])==set(x):
                    ans=ans+1
        return ans
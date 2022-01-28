class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        k=len(s)-1
        c=0
        while(i<k):
            if s[i]==s[k]:
                i=i+1
                k=k-1
            else:
                c=s[i+1:k+1]
                d=s[i:k]
                if s[i+1:k+1]==s[i+1:k+1][::-1]:
                    return True
                if s[i:k]==d[::-1]:
                    return True
                else:
                    return False
        return True
                
            
        
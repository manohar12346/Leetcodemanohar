class Solution:
    def isPalindrome(self, x: int) -> bool:
        d=str(x)
        if d==d[::-1]:
            return True
        return False
        
        
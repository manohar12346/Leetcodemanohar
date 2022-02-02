class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        su=0
        i=0
        while(i<len(s)):
            if i==len(s)-1:
                su=su+dic[s[i]]
                i=i+1
            else:
                if s[i]+s[i+1] in dic:
                    su=su+dic[s[i]+s[i+1]]
                    i=i+2
                else:
                    su=su+dic[s[i]]
                    i=i+1
        sum=su
        return sum
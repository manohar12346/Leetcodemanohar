class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        s=s.split(" ")
        print(s)
        for i in s:
            if i!='':
                ans.append(i)
        ans=ans[::-1]
        return " ".join(ans)
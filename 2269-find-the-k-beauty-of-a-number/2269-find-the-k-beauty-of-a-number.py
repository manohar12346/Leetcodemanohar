class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans=0
        for i  in range((len(str(num))-k)+1):
            d=str(num)[i:i+k]
            print(d)
            if int(d)>0:
                if num%int(d)==0:
                    ans+=1
        return ans
            
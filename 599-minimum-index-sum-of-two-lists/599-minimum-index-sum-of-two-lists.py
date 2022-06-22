class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        x={}
        for i in range(len(list1)):
            x[list1[i]]=i
        mi=10000010
        ans=[]
        for i in range(len(list2)):
            if list2[i] in x:
                if abs(x[list2[i]]+i)<mi:
                    mi=abs(x[list2[i]]+i)
                    del ans
                    ans=[]
                    ans.append(list2[i])
                elif  abs(x[list2[i]]+i)==mi:
                    ans.append(list2[i])
        return ans
        
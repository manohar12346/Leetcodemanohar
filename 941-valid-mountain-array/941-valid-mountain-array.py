class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        c=0
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                if c==2:
                    return False
                c=1
            elif arr[i]>arr[i+1] and (c==1 or c==2):
                c=2
            elif arr[i]>arr[i+1] :
                return False
            else:
                return False
        if c==2:
            return True
        return False
                
        
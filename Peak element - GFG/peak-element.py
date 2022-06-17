# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        i=0
        j=len(arr)-1
        while(i<=j):
            mid=(i+j)//2
            # print(i,j)
            # if mid==0:
            #     if arr[mid+1]<arr[mid]:
                    
            #         return mid
            # if mid==len(arr)-1:
            #     if arr[mid-1]<arr[mid]:
                   
            #         return mid
            # else:
            if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==len(arr)-1 or arr[mid+1]<=arr[mid]):
                
                return mid
            if mid>0 and arr[mid-1]>arr[mid]:
                j=mid-1
            else:
                i=mid+1
    
       


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
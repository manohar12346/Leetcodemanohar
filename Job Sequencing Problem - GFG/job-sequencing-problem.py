#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        x=[]
        for i in Jobs:
            x.append([i.profit,i.deadline])
        x=sorted(x,reverse=True)
        d={}
        c=0
        ans=0
        for i in x:
            if i[1] not in d:
                ans+=i[0]
                d[i[1]]=1
                c+=1
            else:
                for j in range(i[1]-1,0,-1):
                    if j not in d:
                        ans+=i[0]
                        d[j]=1
                        c+=1
                        break
        
        # c=0 
        # ans=0
        # for i in x:
        #     c+=1
        #     ans+=x[i]
        return [c,ans]
        return [0,1]
                    
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends
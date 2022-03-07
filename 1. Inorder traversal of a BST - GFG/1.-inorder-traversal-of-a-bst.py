#{ 
#Driver Code Starts
#Initial Template for Python 3

class Node:
    data=0
    left=None
    right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root
    

    

 # } Driver Code Ends
#User function Template for python3


#Function to return a list containing the inorder traversal of the BST.
def inOrder(root):
    # code here 
    ans=[]
    def inord(root):
        if root==None:
            return 
        else:
            inord(root.left)
            ans.append(root.data)
            
            inord(root.right)
    inord(root)
    return ans

#{ 
#Driver Code Starts.



def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
       
        res = inOrder(root)
        for i in range (len(res)):
            print (res[i], end = " ")
        print()
      
        testcases-=1

if __name__=="__main__":
    main()
#} Driver Code Ends
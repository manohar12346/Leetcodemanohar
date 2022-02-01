class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       
        anse=[]
        def ch(tar,li,index,arr):
            
            if index==len(arr):
               
                if tar==0:
                    x=[]
                    for i in li:
                        x.append(i)
                    
                    anse.append(x)
                    
                
                return
            
            if arr[index]<=tar:
                    li.append(arr[index])
                    ch(tar-arr[index],li,index,arr)
                    li.remove(li[-1])
            
            ch(tar,li,index+1,arr)
        ch(target,[],0,candidates)
        return (anse)
                
                
            
                    
                    
            
                    
            
        
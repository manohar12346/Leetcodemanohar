class MyStack:
    
    def __init__(self):
        self.q1=[]
        self.q2=[]
        return None
    

    def push(self, x: int) -> None:
        for i in range(len(self.q2)):
            self.q1.append(self.q2[i])
        self.q1.append(x)
        self.q2.append(0)
        self.q2[0]=self.q1[-1]
        for i in range(1,len(self.q2)):
            self.q2[i]=self.q1[i-1]
        del self.q1
        self.q1=[]
        print(self.q2)
        
        
        

    def pop(self) -> int:
        print(self.q2)
        c=self.q2[0]
        del self.q2[0]
        return c
        
        

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        if self.q2==[]:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
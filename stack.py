#Pbm 1: Generate valid paranthesis
class Solution:
    def AllParenthesis(self,n):
        if n==0:
            return []
        result=[]
        stack=[('(',1,0)]
        
        while(stack):
            s,left,right=stack.pop()
            
            if len(s)==2*n:
                result.append(s)
                continue
            
            if left<n:
                stack.append((s+'(',left+1,right))
                
            if right<left:
                stack.append((s+')',left,right+1))
        
        return result


#Pbm 2 To get minimum element from stack

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

def push(self,x):
    if  not self.s or self.minEle is None:
        self.s.append(x)
        self.minEle=x
    else:
        if self.minEle is None or x<self.minEle:
            self.s.append((2*x)-self.minEle)
            self.minEle=x
        else:
            self.s.append(x)

def pop(self):
    if not self.s:
        return -1
    y=self.s.pop()
    if y<self.minEle:
        popped_value=self.minEle
        self.minEle=2*self.minEle-y
        return popped_value
    else:
        return y
        
        
def getMin(self):
    if self.s:
        return self.minEle
    else:
        return -1
self.push(5)
self.push(4)
self.push(2)
self.push(7)
self.push(1)
print(self.getMin())
self.pop()
pop()
print(getMin())

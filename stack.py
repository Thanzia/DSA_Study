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

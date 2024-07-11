class Solution:
    def fibonacci(self,n,dp,MOD):
        if n<=1:
            return n
        #if value available take it
        if dp[n]!=-1:
            return dp[n]
        #or calculate and store
        else:
            dp[n]=(self.fibonacci(n-1,dp,MOD)+self.fibonacci(n-2,dp,MOD))%MOD
            return dp[n]
    def series(self, n):
        MOD=1000000007
        l=[]
        #provide an array to store result of eachrecursion tree
        dp=[-1]*(n+1)
        for i in range(n+1):
            l.append(self.fibonacci(i,dp,MOD))
        return l

    #T.C: O(N) S.C:O(N)
    
#for space optimization weuse some pointers alone and avoid dp array
#nthfibonacci number
    def fib(self, n: int) -> int:
        prev2=0
        prev=1
        if n>=1:
            for i in range(2,n+1):
                curr=(prev2+prev)
                prev2=prev
                prev=curr
            return prev
        return 0
    
#fibonacci series    
prev2=0
prev=1
l=[prev2,prev]
for i in range(2,n+1):
    curr=(prev2+prev)%MOD
    prev2=prev
    prev=curr
    l.append(curr)
        #print(l)
            
print(l)

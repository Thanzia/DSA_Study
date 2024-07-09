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

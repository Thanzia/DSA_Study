class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        hash=[0]*26
        l=0
        r=0
        minlen=float('inf')
        sIndex=-1
        cnt=0
        m=len(p)
        for i in range(m):
            hash[ord(p[i])-ord('a')]+=1
        
        while r<len(s):
            if hash[ord(s[r])-ord('a')]>0:
                cnt+=1
            hash[ord(s[r])-ord('a')]-=1
              
            
            while cnt==m:
                if r-l+1<minlen:
                    minlen=r-l+1
                    sIndex=l
                hash[ord(s[l])-ord('a')]+=1
                if hash[ord(s[l])-ord('a')]>0:
                    cnt-=1
                l+=1
                    
            r+=1  
            
        if sIndex==-1:
            return -1
        else:
            return s[sIndex:sIndex+minlen]

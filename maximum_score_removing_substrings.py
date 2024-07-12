class Solution:
    
    def maximumGain(s: str, x: int, y: int) -> int:
        def removepairs(pair,score):
            nonlocal s
            res=0
            stack=[]
            for c in s:
                if c ==pair[1] and stack and stack[-1]==pair[0]:
                    stack.pop()
                    res+=score
                else:
                    stack.append(c)
            s="".join(stack)
            return res
        res=0
        pair="ab" if x>y else "ba"
        res+=removepairs(pair,max(x,y))
        res+=removepairs(pair[::-1],min(x,y))
        return res
    s = "aabbaaxybbaabb"
    x=5
    y = 4
    print(maximumGain(s,x,y))



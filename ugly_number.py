def nthUglyNumber(self, n: int) -> int:
    if n==1:
        return n

    # Initialize DP array for ugly numbers
    ugly=[0]*n
    ugly[0]=1
        
    # Initial multiples of 2, 3, and 5
    next_2=2
    next_3=3
    next_5=5
        
    #pointers for 2 3 5
    i2=i3=i5=0

    for i in range(1,n):
        #choose minimum as the next element
        next_ugly=min(next_2,next_3,next_5)
        ugly[i]=next_ugly

        #update the corresponding number
        if next_ugly==next_2:
            i2+=1
            next_2=ugly[i2]*2
        if next_ugly==next_3:
            i3+=1
            next_3=ugly[i3]*3
        if next_ugly==next_5:
            i5+=1
            next_5=ugly[i5]*5
                
    return ugly[-1]

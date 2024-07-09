#trapping rain water

def trap(self, height: List[int]) -> int:
    n=len(height)
    left=0
    right=n-1
    leftmax=0
    rightmax=0
    res=0
#water stored is found optimally by using the concept
#water @index=min[max.building at right,max.building at left]-current height
    while(left<=right):
        if height[left]<=height[right]:
            if height[left]>=leftmax:
                leftmax=height[left]
            else:
                res+=leftmax-height[left]
            left+=1
        else:
            if height[right]>=rightmax:
                rightmax=height[right]
            else:
                res+=rightmax-height[right]
            right-=1
    return res
        

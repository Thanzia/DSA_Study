def rev(l,r):
    if(l>=r):
        return
    a[l],a[r]=a[r],a[l]
    rev(l+1,r-1)

n=int(input())
a=list(map(int,input().split()))
rev(0,n-1)
print(' '.join(map(str,a)))

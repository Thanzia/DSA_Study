#customers=[[1,2],[2,5],[4,3]]
customers=[[5,2],[5,4],[10,3],[20,1]]
stack=[]
wait_time=0
time=0
l=[]
for i in range(len(customers)):
    if not stack:
        time=customers[i][1]+customers[i][0]
        #print(time)
        wait_time=(time-customers[i][0])
        l.append(wait_time)
        stack.append(time)
        
    
    else:
        #print(time)
        if customers[i][0]<stack[-1]:
            time=stack.pop()+customers[i][1]
        else:
            time=customers[i][0]+customers[i][1]
            stack.pop()
        wait_time=(time-customers[i][0])
        stack.append(time)
        l.append(wait_time)
        #print(wait_time)
    print(wait_time)
    print(stack)
    
print(sum(l)/len(customers))

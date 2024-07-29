'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x:x.profit,reverse=True)
        maxi=Jobs[0].deadline
        for i in range(1,len(Jobs)):
            maxi=max(maxi,Jobs[i].deadline)
        slot=[-1]*(maxi+1)
        countJobs=0
        jobProfit=0
        for i in range(len(Jobs)):
            for j in range(Jobs[i].deadline,0,-1):
                if slot[j]==-1:
                    slot[j]=i
                    countJobs+=1
                    jobProfit+=Jobs[i].profit
                    break
        return countJobs,jobProfit

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        count=0
        #rating[j]as the middle element find strictly increasing or decreasing by 
        #left_smaller * right_larger(strictly increasing) and 
        #left_larger * right_smaller(strictly decreasing )
        for j in range(n):
            left_smaller = 0
            left_larger = 0
            right_smaller = 0
            right_larger = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1
            
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                elif rating[k] < rating[j]:
                    right_smaller += 1
            
            count += left_smaller * right_larger + left_larger * right_smaller
        
        
        return count

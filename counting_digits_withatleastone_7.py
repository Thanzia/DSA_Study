#pbm1:counting N digit numbers with a 7
#given a positive integer n,count the number of n digit numbers
#that contain at least one digit 7 since the answer could be large
#compute it modulo 10^9+7

class Solution:
    def countWays(self, n : int) -> int:
        MOD=1000000007
        if n<=0:
            return 0
        power_10 = 1
        power_9 = 1
        #to find the power of 10 and 9 optimally else tle
        def power(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result

        #The total number of n digit numbers is 9x10^(n-1)
        #first digit ranges from 1 to 9 and remaining (n-1) digits ranges from 0 to 9
        #total=9x10^(n-1)
        #when 7 excluded: first digit 1...6,8,9(8numbers)and remaining (n-1)
        #digits ranges from 0...6,8,9(total 9)
        #without_7=8x9^(n-1)

        power_10=power(10,n-1,MOD)
        power_9=power(9,n-1,MOD)
        total=(9*power_10)%MOD
        without_7=(8*power_9)%MOD
        numbers_with_7=(total-without_7+MOD)%MOD
        return numbers_with_7

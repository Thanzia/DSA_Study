#pbm: check if Array Pairs are divisible by k
#We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
#Return true If you can find a way to do that or false otherwise.

from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)
    
        # Count the remainder of each element when divided by k
        for num in arr:
            remainder = num % k
            # Handle negative remainders by making them positive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1

        # Check if we can form pairs
        for remainder in list(remainder_count.keys()):
            if remainder == 0:
                # Special case: remainder 0 must pair with itself
                if remainder_count[remainder] % 2 != 0:
                    return False
            elif remainder == k // 2 and k % 2 == 0:
                # Special case for even k, remainder k/2
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                complement = k - remainder
                if remainder_count[remainder] != remainder_count[complement]:
                    return False

        return True

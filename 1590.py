#Make sum divisible by p

'''Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.'''

 

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0  # No need to remove any subarray, already divisible by p
    
        # Hash map to store the last occurrence of a prefix sum % p
        prefix_mod_map = {0: -1}  # Initialize with 0 remainder at index -1 (before the start of the array)
        current_prefix = 0
        min_length = len(nums)
    
        for i, num in enumerate(nums):
            current_prefix += num
            current_prefix %= p
        
            # We want (current_prefix - remainder) % p == 0
            target_mod = (current_prefix - remainder) % p
        
            if target_mod in prefix_mod_map:
                min_length = min(min_length, i - prefix_mod_map[target_mod])
        
            # Update the map with the current prefix mod and its index
            prefix_mod_map[current_prefix] = i
    
        # If we found a valid subarray, return its length, otherwise return -1
        return min_length if min_length < len(nums) else -1


        

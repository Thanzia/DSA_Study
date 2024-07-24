class Solution:
    def map_value(self,num, mapping):
        # Convert number to string for digit-by-digit manipulation
        num_str = str(num)
        mapped_num_str = ''
        for char in num_str:
            mapped_num_str += str(mapping[int(char)])
        # Convert mapped string back to integer to avoid leading zeros issues
        return int(mapped_num_str)
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Create a list of tuples (mapped_value, original_number)
        mapped_nums = [(self.map_value(num, mapping), num) for num in nums]
        # Sort by the mapped value (first element of the tuple)
        mapped_nums.sort(key=lambda x: x[0])
        # Extract the original numbers in the sorted order
        sorted_nums = [num for _, num in mapped_nums]
        return sorted_nums


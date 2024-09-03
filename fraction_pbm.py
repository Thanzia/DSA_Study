from fractions import Fraction
import re
from math import gcd
expression="-1/2+1/2+1/3"
def fractionAddition(expression: str) -> str:
    nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
    print(nums)
    numerator = 0
    denominator = 1
        
    for i in range(0, len(nums), 2):
        num, den = nums[i], nums[i + 1]
        numerator = numerator * den + num * denominator
        denominator *= den
        
    common_divisor = gcd(numerator, denominator)
    return f"{numerator // common_divisor}/{denominator // common_divisor}"
print(fractionAddition(expression))
        

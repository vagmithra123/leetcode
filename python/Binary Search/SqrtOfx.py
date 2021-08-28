'''
69. Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        low, high = 0, x-1
        while(low < high):
            mid = (low + high)//2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                low = mid+1
            else:
                high = mid-1
            
        if low * low <= x:
            return low
        else:
            return low-1
                
    
        
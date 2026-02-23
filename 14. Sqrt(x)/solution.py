class Solution:
    def mySqrt(self, x: int) -> int:
        # left starts at 1, right at x // 2 since sqrt(x) cannot exceed x/2 for x >= 2
        left, right = 1, x // 2
        # Continue searching while the range is valid
        while left <= right:
            mid = (left + right) // 2  # Calculate midpoint to test a candidate square root
            if mid * mid == x:
                return mid 
            elif mid * mid < x:
                left = mid + 1
            else: right = mid - 1
        
        return right 

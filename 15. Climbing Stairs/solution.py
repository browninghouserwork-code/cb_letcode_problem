class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2
        # commit: iterate from step 3 up to n to build solutions incrementally
        for i in range(3, n + 1):
            third = first + second # commit: current ways = sum of previous two steps (Fibonacci relation)
            # commit: update previous step values
            first = second
            second = third 
    
        return second

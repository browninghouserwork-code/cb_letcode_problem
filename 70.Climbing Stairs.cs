public class Solution
{
    public int ClimbStairs(int n)
    {
        if (n <= 2) return n;

        int a = 1, b = 2; // climbing method is 2 ways
        for (int i = 3; i <= n; i++)
        {
            int temp = a + b;
	//f(n)=f(n−1)+f(n−2)
	// why above?  :  1 step from n-1, or 2 steps from n-2
            a = b;
            b = temp;
        }
        return b;
    }
}

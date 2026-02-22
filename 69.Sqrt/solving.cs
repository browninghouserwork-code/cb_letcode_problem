public class Solution
{
    public int MySqrt(int x)
    {
        int i = 0;
        while ((long)i * i <= x) i++; 
        return i - 1;                  
    }
}

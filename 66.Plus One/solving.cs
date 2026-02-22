public class Solution
{
    public int[] PlusOne(int[] digits)
    {
        for (int i = digits.Length - 1; i >= 0; i--)
        {
            digits[i]++;           // Add 1
            if (digits[i] < 10)    
                return digits;
            digits[i] = 0;         // Over 10
        }

        // If all digits were 9, result is 100...0
        int[] result = new int[digits.Length + 1];
	// do not format, so auto fill 0
        result[0] = 1;
	// first number is 1
        return result;
    }
}

public class Solution
{
    public string AddBinary(string a, string b)
    {
        int sum = Convert.ToInt32(a, 2) + Convert.ToInt32(b, 2);
	// convert string to int
        return Convert.ToString(sum, 2);
    }
}

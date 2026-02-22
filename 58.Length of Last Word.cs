public class Solution
{
    public int LengthOfLastWord(string s)
    {
        // Trim: remove spaces from both ends of string
        s = s.Trim();

        // LastIndexOf(' '): Find the last space
        int lastSpace = s.LastIndexOf(' ');

        // Length of last word = total length - index of last space - 1
        return s.Length - lastSpace - 1;
    }
}

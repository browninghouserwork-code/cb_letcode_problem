public class Solution
{
    public int StrStr(string haystack, string needle)// StrStr is required name from platform!
    {
        return haystack.IndexOf(needle);	//if needle is "", return value is 0.
    }
}

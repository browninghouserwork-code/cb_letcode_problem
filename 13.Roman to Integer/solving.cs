using System;
using System.Collections.Generic;

public class Solution
{
    public int RomanToInt(string s)
    {
	// creat new dictionary(similar with class) for saving Roman and number pairs
        Dictionary<char, int> romanMap = new Dictionary<char, int>
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };
	// format sum of Roman
        int total = 0;
        // start to finish loop Roman string
        for (int i = 0; i < s.Length; i++)
        {
	// Compare selected Roman and next Roman (value)
            if (i < s.Length - 1 && romanMap[s[i]] < romanMap[s[i + 1]])
            {
	// if next Roman > selected Roman(value), reduce value of selected Roman 
                total -= romanMap[s[i]];
            }
            else
            {
                total += romanMap[s[i]];
            }
        }

        return total;
    }
}
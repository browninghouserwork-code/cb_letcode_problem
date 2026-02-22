using System;
using System.Collections.Generic;

public class Solution
{
    public bool IsValid(string s)
    {
        Stack<char> stack = new Stack<char>();
        Dictionary<char, char> pairs = new Dictionary<char, char>
        {
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };

        foreach (char ch in s)
        {
            // Opening bracket
            if (pairs.ContainsValue(ch))
            {
                stack.Push(ch);
            }
            // Closing bracket
            else
            {
                if (stack.Count == 0 || stack.Peek() != pairs[ch])
	    // stack.Peek() is the top of current stack, ch: current closing char, pairs[ch]: matching opening char with ch
                    return false;

                stack.Pop();	// remove matching opening bracket
            }
        }

        return stack.Count == 0;	// if stack is blank, true!
    }
}

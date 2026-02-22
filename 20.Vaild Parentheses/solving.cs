using System;
//The using System.Collections.Generic; statement in C# is used to import the System.Collections.Generic namespace, which contains classes and interfaces that define generic collections

using System.Collections.Generic;

public class Solution
{
    public bool IsValid(string s)
    {
// creat new stack(stack is collection for saving char by LIFO(last in, first out) way)
        Stack<char> stack = new Stack<char>();
// creat new dictionary for saving bracket pairs: key:close bracket value:open bracket
        Dictionary<char, char> pairs = new Dictionary<char, char>
        {
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };
// loop each char in inputed string
        foreach (char ch in s)
        {
            // pairs.ContainsValue(ch): only value of pair - Opening bracket
            if (pairs.ContainsValue(ch))
            {
                stack.Push(ch);
            }
            // Closing bracket
            else
            {
                if (stack.Count == 0 || stack.Peek() != pairs[ch]
// stack.Peek() is the top of current stack, ch: current closing char, pairs[ch]: matching opening char with ch
                    return false;

                stack.Pop();	// remove matching opening bracket
            }
        }

        return stack.Count == 0;	// if stack is blank, true!
    }
}

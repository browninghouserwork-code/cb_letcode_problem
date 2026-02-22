using System;

//LINQ (Language Integrated Query)
C# supports LINQ, which allows you to query collections (like arrays or lists) in a declarative way.

using System.Linq;	

public class Solution {
    public bool IsPalindrome(int x) {
	// int convert to string using Convert.ToString(x)
        String num = Convert.ToString(x);
	// creat new string: reverse first string-num and conver to array
        String num1 = new string (num.Reverse().ToArray());
	// compare two string
        if(num == num1){
            return true;
        }
        else {
            return false;
        }

    }
}
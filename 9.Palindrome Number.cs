using System;
using System.Linq;

public class Solution {
    public bool IsPalindrome(int x) {
        String num = Convert.ToString(x);
        String num1 = new string (num.Reverse().ToArray());
        if(num == num1){
            return true;
        }
        else {
            return false;
        }

    }
}
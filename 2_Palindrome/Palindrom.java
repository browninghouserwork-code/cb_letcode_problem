// Palindrome Number
// Given an integer x, return true if x is a palindrome, and false otherwise.

let x = 121;

function isPalindrome(x) {
    if (x < 0) return false;
    if (x === 0) return true;
    let str = x.toString();
    let left = 0;
    let right = str.length - 1;
    while (left < right) {
        if (str[left] !== str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
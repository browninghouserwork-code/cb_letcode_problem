var isPalindrome = function(x) {
    if (x < 0) return false;  // negatives aren't palindromes
    if (x % 10 === 0 && x !== 0) return false;  // trailing zero (except 0 itself)
    
    let str_x = x.toString();
    let str_x_reversed = str_x.split('').reverse().join('');
    return str_x === str_x_reversed;
};

console.log(isPalindrome(121));    // true
console.log(isPalindrome(-121));   // false
console.log(isPalindrome(10));     // false
// 13. Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

var romanToInt = (s) => {
    const romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    // Iterate from right-to-left; if current < previous seen value, subtract, else add.
    let total = 0;
    let prev = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        const curr = romanMap[s[i]];
        if (curr < prev) total -= curr;
        else { total += curr; prev = curr; }
    }
    return total;
}

// Test cases
console.log(romanToInt("III")); // expected 3
console.log(romanToInt("IV")); // expected 4
console.log(romanToInt("IX")); // expected 9
console.log(romanToInt("LVIII"));   // expected 58 
console.log(romanToInt("MCMXCIV")); // expected 1994
console.log(romanToInt("MMXXIV")); // expected 2024
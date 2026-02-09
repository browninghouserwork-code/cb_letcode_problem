// Two Sum
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

let num = [2, 7, 11, 15];
let target = 9;

// let result = [];

// Optimized O(n) solution using a hash map (single-pass)
function twoSum(nums, target) {
    const seen = new Map();
    // console.log(seen);
    for (let i = 0; i < nums.length; i++) {
        const need = target - nums[i];
        if (seen.has(need)) return [seen.get(need), i];
        seen.set(nums[i], i);
    }
    return null;
}

console.log(twoSum(num, target)); // expected [0,1]
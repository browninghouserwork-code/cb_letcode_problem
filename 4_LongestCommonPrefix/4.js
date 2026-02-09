// 14. Longest Common Prefix
// Given an array of strings, write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

let strs = ["flower", "flow", "flight"];
function longestCommonPrefix(strs) {
    if (strs.length === 0) return "";
    let prefix = strs[0];
    for (let i = 1; i < strs.length; i++) {
        console.log(prefix);
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.substring(0, prefix.length - 1);
            console.log(prefix);
            if (prefix === "") return "";
        }
    }
    return prefix;
}
console.log(longestCommonPrefix(strs));

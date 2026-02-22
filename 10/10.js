const haystack1 = "sadbutsad"
const needle1   = "sad"

function strStr(haystack, needle) {
    let n = haystack.length;
    let m = needle.length;

    if (m > n) return -1;

   
    for (let i = 0; i <= n - m; i++) {
        let j = 0;

        while (j < m && haystack[i + j] === needle[j]) {
            j++;
        }

        if (j === m) {
            return i;
        }
    }

    return -1;
}

console.log(strStr(haystack1,needle1));
const nums1 = [3,2,2,3], val1 = 3

function removeElement(nums, val) {
    let k = 0; // Index for non-val elements

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
}

console.log(removeElement(nums1,val1));
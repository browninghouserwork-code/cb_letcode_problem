class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        
        k = 1
        # Start iterating from the second element to the end of the list.
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique.
            if nums[i] != nums[i - 1]:
                nums[k] = nums [i] # Place the unique element at index k.
                k += 1
        
        return k  # Return k

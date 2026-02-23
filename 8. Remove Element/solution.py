class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        # commit: iterate through each index of the nums list
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

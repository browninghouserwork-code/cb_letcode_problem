class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1  # set pointer i at last valid element of nums1  
        j = n - 1  # set pointer j at last element of nums2 
        k = m + n - 1  # set pointer k at last position of nums1 
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i] # place larger element from nums1 at position k
                i -= 1 # move nums1 pointer left
            else:
                nums1[k] = nums2[j] # place larger element from nums2 at position k
                j -= 1 # move nums2 pointer left
            k -= 1 # move merge pointer left
        while j >= 0:
            nums1[k] = nums2[j] # copy remaining nums2 elements into nums1
            j -= 1
            k -= 1

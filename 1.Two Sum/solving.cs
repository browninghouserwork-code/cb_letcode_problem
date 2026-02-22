public class Solution {
    public int[] TwoSum(int[] nums, int target) {
	// first loop - select first adding value
       for (int i = 0; i < nums.Length; i++)
       {
	// second loop - select second adding value
        for (int j = i + 1; j < nums.Length; j++)
        {
	// compare with target
         if (nums[i] + nums[j] == target)
         {
            return new int[] {i, j};
         }   
        }
       } 
       return new int[] {}; 
    }
}
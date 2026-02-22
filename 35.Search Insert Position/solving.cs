public class Solution
{
    public int SearchInsert(int[] nums, int target)
    {
        int index = Array.BinarySearch(nums, target);	
	// if target exist, return index, return-insertion point
        return index >= 0 ? index : ~index;
	//~: bitwise NOT(-insertion point-1)		
    }
}

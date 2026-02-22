public class Solution {
    public string LongestCommonPrefix(string[] strs) {
	// select compair thing  as strs[0](first string)
        string pre = strs[0];
	// loop each char in pre(first string)
        for(int i = 0; i < pre.Length; i++){
 	    // create searching string as common
            string common = pre.Substring(0, i+1);
	    // common compair with each strings
            for(int j = 1; j < strs.Length; j++){
		// when any strs do not contain common, return just past common string
                if(!strs[j].Contains(common)){
                    return pre.Substring(0,i);
                }
            }
        }
        return pre;
    }
}
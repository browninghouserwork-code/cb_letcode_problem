public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string pre = strs[0];
        for(int i = 0; i < pre.Length; i++){
            string common = pre.Substring(0, i+1);
            for(int j = 1; j < strs.Length; j++){
                if(!strs[j].Contains(common)){
                    return pre.Substring(0,i);
                }
            }
        }
        return pre;
    }
}
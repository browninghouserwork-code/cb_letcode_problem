# 14. Longest Common Prefix
# Given an array of strings, write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".


# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# Test cases
solution = Solution()
print(
    solution.longestCommonPrefix(["flower", "flow", "flight"])
)  # Expected output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  # Expected output: ""

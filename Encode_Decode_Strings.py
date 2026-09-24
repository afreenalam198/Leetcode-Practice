# Leetcode 271. Encode and Decode Strings

# Problem Statement:
# Design an algorithm to encode a list of strings to a string. T
# The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }
# So Machine 1 does:

# String encoded_string = encode(strs);
# and Machine 2 does:
# List<String> decoded_strs = decode(encoded_string);
# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:
# Input: strs = ["Hello","World"]
# Output: ["Hello","World"]

# Explanation:
# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

# // Machine 1 ---encoded_string---> Machine 2

# List<String> decoded_strs = solution.decode(encoded_string);

# Example 2:
# Input: strs = [""]
# Output: [""]

# Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Recommended Time and Space Complexity:
# Time Complexity: O(m) for each encode() and decode() call
# Space Complexity: O(m+n), where m is the sum of lengths of all the strings and n is the number of strings.

class Solution:

    def encode(self, strs: list[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        while i < len(s):
            count = ""
            j = i
            while s[j] != '#':
                count += s[j]
                j += 1
            count = int(count)
            start = j+1
            end = start+count
            result.append(s[start : end])

            i = end

        return result

if __name__ == "__main__":
    solution = Solution()
    
    strs = ["Hello","World"]
    encoded_string = solution.encode(strs)
    print("Encoded String:", encoded_string)
    decoded_strs = solution.decode(encoded_string)
    print("Decoded Strings:", decoded_strs)

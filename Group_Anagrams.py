# Leetcode 49: Group Anagrams

# Problem Statement:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Recommended Time and Space Complexity:
# Time Complexity: O(m * n), where m is the number of strings and n is the length of the longest string.
# Space Complexity: O(m)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1. Create an empty dictionary (key - freq array, value - words array)
        # 2. Loop through the input array
        # 3. Create a frequency array of size 26 for the current word, that will be the dictionary key
        # 4. Check if the key exists in dict, if not create a new key value pair
        # 5. If key exists, update the value by adding the current word to the array
        # 6. Loop through the dict values and add them to the result array

        anagram_dict = dict()
        for word in strs:
            # Key creation - frequency array
            freq_arr = [0]*26
            for letter in word:
                freq_arr[ord(letter)-ord('a')] += 1
            # Convert freq arr to tuple because keys cannot be mutable
            freq = tuple(freq_arr)
            if freq not in anagram_dict:
                anagram_dict[freq] = [word]
            else:
                anagram_dict[freq].append(word)
        result = []
        for val in anagram_dict.values():
            result.append(val)
        return result

if __name__ == "__main__":
    solution = Solution()

    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(solution.groupAnagrams([""])) # Output: [[""]]
    print(solution.groupAnagrams(["a"])) # Output: [["a"]]
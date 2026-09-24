# Leetcode 242: Valid Anagram

# Problem Statement:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Recommended Time and Space Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force Solution (Time Complexity: O(nlogn), Space Complexity: O(1)) -
        # 1. Check if length of s and t are equal
        # 2. Sort s and t
        # 3. Check if s and t are equal
        # 4. If equal, return True
        # 5. Else, return False

        # if len(s) != len(t):
        #     return False
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # Optimized Solution (Time Complexity: O(n**2), Space Complexity: O()) -
        # 1. Check if length of s and t are equal
        # 2. Convert s and t to hashtables using Counter for letter frequency
        # 3. Check if hashtables of a and t are equal
        # 4. If yes, return True
        # 5. Else, return False

        if len(s) != len(t):
            return False
        hash_s = Counter(s)
        hash_t = Counter(t)
        if hash_s == hash_t:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()

    print(solution.isAnagram("anagram", "nagaram")) # Output: True
    print(solution.isAnagram("rat", "car")) # Output: False
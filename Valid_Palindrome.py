# Leetcode 125: Valid Palindrome

# Problem Statement:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Recommended Time and Space Complexity:
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Use two pointers to check lowercase converted char from left to lowercase converted char from right until halfway point
        # 2. Use a helper function to check if a char is alphanumeric
        # 3. If char is not alphanumeric, then skip
        # 4. If mismatch found, then return False
        # 5. Otherwise, return True


        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNumeric(self, c: str) -> bool:
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )



if __name__ == "__main__":
    solution = Solution()

    print(solution.isPalindrome("A man, a plan, a canal: Panama")) # True
    print(solution.isPalindrome("race a car")) # False
    print(solution.isPalindrome(" ")) # True
        
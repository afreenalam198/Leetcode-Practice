# Leetcode 217: Contains Duplicate

# Problem Statement:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Recommended Time and Spce Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Brute Force Solution (Time Complexity: O(n**2), Space Complexity: O(1)) -
        # 1. Use nested loops 
        # 2. Compare each element of the outer loop against each element of the inner loop
        # 3. If match found, return True
        # 4. Else continue and return False after outer loop is completed 

        # Optimized Solution (Time Complexity: O(n), Space Complexity: O(n)) -
        # 1. Convert array to set
        # 2. Compare length of array and set
        # 3. If equal, return False
        # 4. Else, return True

        nums_set = set(nums)

        if len(nums_set) != len(nums):
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()

    print(solution.containsDuplicate([1, 2, 3, 1])) # Output: True
    print(solution.containsDuplicate([1, 2, 3, 4])) # Output: False

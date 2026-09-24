# Leetcode 1: Two Sum

# Problem Statement:
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Recommended Time and Space Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. Create a dictionary
        # 2. Loop through the input array
        # 3. Check if current index value exists in dict
        # 4. If it does not exist, then subtract from target and insert as key and value would be an array containing the current index
        # 5. If it exists, append current index to the value array
        # 6. Return the value array

        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[target-nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)
                return hashmap[nums[i]]

if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2,7,11,15], 9)) # Output: [0,1]
    print(solution.twoSum([3,2,4], 6)) # Output: [1,2]
    print(solution.twoSum([3,3], 6)) # Output: [0,1]
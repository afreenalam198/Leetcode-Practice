# Leetcode 347: Top K Frequent Elements

# Problem Statement:
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# # It is guaranteed that the answer is unique.

# Recommended Time and Space Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Create a frequency hashmap 
        # 2. Loop through the array to fill up the hashmap (Key - Index element, Value - Count)
        # 3. Create a freq array of the same size as input array
        # 4. Loop through the hashmap k,v pairs and fill out the freq array, where
        #    v - index, k - array of index elements
        # Create a result array
        # 5. Loop through the freq array in reverse 
        # 6. Append index element vals into result array
        # 7. Check if len of result array = target
        # 8. If yes, break out and return result array
        # 9. Otherwise, continue

        freq_map = {}
        for i in range(len(nums)):
            if nums[i] not in freq_map:
                freq_map[nums[i]] = 1
            else:
                freq_map[nums[i]] += 1

        freq_arr = [0]*(len(nums)+1)

        for key,val in freq_map.items():
            if freq_arr[val] != 0:
                freq_arr[val].append(key)
            else:
                freq_arr[val] = [key]


        result_arr = []
        for i in range(len(freq_arr)-1, -1, -1):
            if freq_arr[i] != 0:
                if len(result_arr) != k:
                    result_arr.extend(freq_arr[i])
                else:
                    break
        return result_arr

if __name__ == "__main__":
    solution = Solution()

    print(solution.topKFrequent([1,1,1,2,2,3], 2)) # Output: [1,2]
    print(solution.topKFrequent([1], 1)) # Output: [1]
    print(solution.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)) # Output: [1,2]
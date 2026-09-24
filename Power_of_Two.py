# Leetcode 231: Power of Two

# Problem Statement:
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: n = 3
# Output: false
 
# Constraints:
# -231 <= n <= 231 - 1

# Recommended Time and Space Complexity:
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # If we perform Bit-wise AND operation
        # on the binary of int, n that is a power of 2 
        # and binary of int, n-1
        # then the result will always be 0
        # If int, n is not a power of two,
        # then doing the same would not result in 0
        # n = 5, n-1 = 4
        # bin -   0101
        #         0100
        # Bit-wise AND operation = 0100
        # n = 4, n-1 = 3
        # bin -   0100
        #         0011
        # Bit-wise AND operation = 0000
        # n <= 0 check makes sure that no negative numbers or 0 triggers the True condition
        if n <= 0 or (n & n-1) != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    solution = Solution()
    
    print(solution.isPowerOfTwo(1))  # True
    print(solution.isPowerOfTwo(16))  # True
    print(solution.isPowerOfTwo(3))  # False
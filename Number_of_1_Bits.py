# Leetcode 191: Number of 1 Bits

# Problem Statement:
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3

# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1

# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30

# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

# Constraints:
# 1 <= n <= 231 - 1

# Recommended Time and Space Complexity:
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Brute Force Built-in Method Solution -
        # 1. Convert n to binary representation
        # 2. Loop through the binary rep. and 
        # 3. increment a counter if 
        # 4. current index value is 1
        # binN = bin(n)[2:]
        # count = 0
        # for digit in binN:
        #     if int(digit) == 1:
        #         count += 1
        # return count

        # Optimal Bit Manipulation Solution -
        # 1. Initialize a count variable
        # 2. Use a while loop until n is not zero
        # 3. n = bit wise and operation of n and n-1
        # 4. increment count
        # Subtracting 1 from a bin num flips the rightmost 1 bit to 0 and every bit to the right of it to 1
        # When we do n & n-1, we are getting rid of 
        # n - 11
        # 1011
        # 1010
        # 1010 --> +1
        # 1001
        # 1000 --> +1
        # 0110 
        # 0000 --> +1

        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    
    print(solution.hammingWeight(11))  # 3
    print(solution.hammingWeight(128))  # 1
    print(solution.hammingWeight(2147483645))  # 30

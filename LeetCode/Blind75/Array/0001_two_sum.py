"""
Problem: Two Sum
=================

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers
such that they add up to `target`.

Assumptions:
1. Each input will have exactly one solution.
2. You may not use the same element twice.
3. The answer can be returned in any order.

Examples:
---------

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:
------------
1. 2 <= nums.length <= 10^4
2. -10^9 <= nums[i] <= 10^9
3. -10^9 <= target <= 10^9
4. Only one valid answer exists.
"""
#
"""
Thought Process:
TODO - Add the thought process here


---------
"""



from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Approach: Hash Map
    ==================
    This approach uses a hash map (dictionary in Python) to store previously seen numbers and their indices
    while iterating through the list. It allows us to check if the complement (target - current number)
    exists in constant time O(1).

    Steps:
    ------
    1. Create an empty hash map to store numbers and their indices.
    2. For each number in the list:
        a. Calculate its complement (target - current number).
        b. If the complement is found in the hash map, return the indices of the complement and the current number.
        c. Otherwise, add the current number and its index to the hash map.
    3. If no solution is found (shouldn't happen due to constraints), return an empty list.

    Time Complexity: O(n) - We traverse the list once and perform O(1) operations for each element.
    Space Complexity: O(n) - We store at most n elements in the hash map.

    Parameters:
    -----------
    nums : List[int]
        The list of integers.
    target : int
        The target sum.

    Returns:
    --------
    List[int]
        Indices of the two numbers that add up to the target.
    """
    # Start your implementation here:

    return []


# Main function to run the test cases
if __name__ == '__main__':
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Example 1 Output:", twoSum(nums1, target1))  # Expected: [0, 1]

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("Example 2 Output:", twoSum(nums2, target2))  # Expected: [1, 2]

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    print("Example 3 Output:", twoSum(nums3, target3))  # Expected: [0, 1]

    """ 
    Solution: 
    
    # # Hash map to store numbers and their indices
    # hash_map = {}

    # # Iterate through the list
    # for i, num in enumerate(nums):
    #     # Calculate the complement
    #     complement = target - num

    #     # Check if the complement exists in the hash map
    #     if complement in hash_map:
    #         return [hash_map[complement], i]  # Return the indices of the complement and the current number

    #     # Add the current number to the hash map
    #     hash_map[num] = i

    # Default return (not expected to be reached due to problem constraints)
    
    """

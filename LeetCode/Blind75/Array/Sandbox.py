

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    Hashmap = {}

    


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

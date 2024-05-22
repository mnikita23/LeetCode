class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the subsets
        subsets = []
        # Call the helper function with an empty list and the index 0
        self.backtrack(nums, [], subsets, 0)
        # Return the list of subsets
        return subsets

    def backtrack(self, nums: List[int], subset: List[int], subsets: List[List[int]], index: int) -> None:
        # Add the current subset to the list of subsets
        subsets.append(subset.copy())
        # Iterate through the remaining elements in the nums list
        for i in range(index, len(nums)):
            # Add the current element to the subset
            subset.append(nums[i])
            # Call the helper function with the updated subset and the index increased by 1
            self.backtrack(nums, subset, subsets, i + 1)
            # Remove the last element from the subset
            subset.pop()

# Example usage
nums = [1, 2, 3]
solution = Solution()
print(solution.subsets(nums))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

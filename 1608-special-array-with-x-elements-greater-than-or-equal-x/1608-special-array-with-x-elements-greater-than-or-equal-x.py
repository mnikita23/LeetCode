from bisect import bisect_left

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Sort the input array.
        nums.sort()
      
        # Find the length of the nums array and store it in a variable n.
        n = len(nums)

        # Iterate through potential special values (x).
        for x in range(1, n + 1):
            # Use binary search (bisect_left) to find the leftmost position in nums
            # where x could be inserted, then subtract it from n to get the count 
            # of elements greater than or equal to x.
            count_greater_or_equal_to_x = n - bisect_left(nums, x)
          
            # Check if count is equal to x (which is our definition of a special array).
            if count_greater_or_equal_to_x == x:
                # If it is a special array, return x.
                return x
              
        # If no special value is found, return -1.
        return -1

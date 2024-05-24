class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Return 0 if nums is empty
        if not nums:
            return 0
            
        i = 0 
        j = 1
        dup = 1
        while i < len(nums) and j < len(nums):
            # If items are equal
            if nums[i] == nums[j]:
                # If no consecutive items, increment i and swap with j
                if dup < 2:
                    i = i + 1
                    nums[i], nums[j] = nums[j], nums[i]
                # If consecutive items exist, increment j and increase dup
                j = j + 1
                dup += 1
            else:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i] 
                j = j + 1
                dup = 1
        return i + 1
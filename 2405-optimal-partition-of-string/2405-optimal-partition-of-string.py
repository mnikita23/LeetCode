class Solution:
    def partitionString(self, s: str) -> int:
        # Initialize the number of substrings to 1
        substrings = 1
        
        # Initialize a set to keep track of the characters in the current substring
        current_set = set()
        
        # Iterate over the characters in the string
        for char in s:
            # If the character is already in the current set, increment the number
            # of substrings by 1
            if char in current_set:
                substrings += 1
                # Clear the current set and add the new character to it
                current_set.clear()
                current_set.add(char)
            # Otherwise, add the character to the current set
            else:
                current_set.add(char)
        
        # Return the number of substrings
        return substrings
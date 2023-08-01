# # Approach 1 - Brute Force
# Double loop - Checking with every element in the array 
# TC - O(n^2)
# SC - O(1)

# # Approach 2 - Sorting
# Sort Array - Checking adjacent elements till we get duplicates
# TC - O(nlogn)
# SC - O(1)

# # Approach 3 - Hash Set
# Checking if hash set has encountered that element, or else add that element to the hash
# TC - O(n)
# SC - O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    hs = set()
    for num in nums:
        if num in hs:
            return True
        hs.add(num)
    return False

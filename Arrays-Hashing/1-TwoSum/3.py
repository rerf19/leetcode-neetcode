#Solution with HashTable
# knowing that I just needed to know if the difference was in the previous previous numbers
# I just needed to check if the difference was in the hashtable
# and if not just add to the hashtable

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ht = {}

        i = 0
        for n in nums:
            diff = target - n
            if diff in ht:
                return [ht[diff], i]
            
            ht[n] = i
            i = i + 1
#use a hashmap

#the best solution
class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        map = set()

        for i in nums:
            if i in map:
                return False
            else:
                map.add(i)

        return True
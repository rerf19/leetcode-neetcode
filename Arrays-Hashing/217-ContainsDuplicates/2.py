#Use Sort and then check

class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #bubble sort 
        n = len(nums)

        for i in range(n-1):
            for j in range(0,n-i-1):

                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        #check if there is any repeated numbers
        for i in range(n-1):
            if( nums[i] == nums[i+1]):
                return True

        return False

#Time Complexity: O(nlogn)
#Space: O(1)
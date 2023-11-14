class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            print(nums[i])
            for j in range(len(nums)):
                if(i != j):
                    if(nums[i] == nums[j]):
                        return True
        return False
    
#Time Complexity: 0(n^2)
#Space: 0(n)

#this solutions if basicly brute force all the numbers
#whem submited it gave the error "TIME LIMIT EXCEDED"
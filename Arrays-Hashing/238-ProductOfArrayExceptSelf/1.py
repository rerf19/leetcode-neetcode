# I know this solution is wrong, but it was the only  one that came to my mind 
# after an hour of thinking.

def productExceptSelf(nums):
    print(nums)
    
    m = 1
    for i in nums:
        if i != 0:
            m = m * i

    for count,n in enumerate(nums):
        if n != 0:
            nums[count] = m/n

    return nums




nums = [-1,1,0,-3,3]
r = productExceptSelf(nums)
print (r)
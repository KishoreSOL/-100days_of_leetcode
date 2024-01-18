class Solution(object):
    def rotate(self, nums, k):
        
        if k > len(nums):
            k = k % len(nums)

        i = 0
        j = len(nums) - k -1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i +=1
            j-=1
        
        i = len(nums) - k
        j = len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i +=1
            j-=1
        
        return nums.reverse()


            
        
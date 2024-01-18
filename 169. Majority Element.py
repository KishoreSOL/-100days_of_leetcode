class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        index=0
        maxx=0
        k=1
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                k+=1
            else:
                k=1
            if maxx <= k:
                maxx=k
                index=i
        return nums[index]
        
            
            

        
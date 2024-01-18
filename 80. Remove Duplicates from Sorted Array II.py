class Solution(object):
    def removeDuplicates(self, nums):
        flag=0
        l=len(nums)
        i=1
        while i<l:
            if nums[i]==nums[i-1]:
                if flag==1:
                    nums.remove(nums[i])
                    l-=1
                    i-=1
                flag=1
            else:
                flag=0
            i+=1
        return l
        
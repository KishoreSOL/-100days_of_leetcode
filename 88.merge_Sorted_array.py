class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while(1):
            if(len(nums1)>m):
                nums1.pop()
                continue
            break
        while(1):
            if(len(nums2)>n):
                nums2.pop()
                continue
            break
        nums1+=nums2
        return nums1.sort()
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sz = len(nums)
        if(sz==0):
            return 0
        if(sz==1):
            return nums[0]
        if(sz==2):
            return(max(nums[0],nums[1]))
        for i in range(2,sz):
            maxi = 0
            for j in range(0,i-1):
                if(nums[j]>maxi):
                    maxi = nums[j]
            nums[i] += maxi
        return max(nums[sz-1],nums[sz-2])
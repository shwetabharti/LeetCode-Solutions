class Solution(object):
    def moveZeroes(self, nums):
        sz = len(nums)
        count = 0;
        for i in range(0,sz):
            if(nums[i]!=0):
                if(count!=i):
                    nums[count] = nums[i]
                    nums[i] = 0
                count += 1;
        
            
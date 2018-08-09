class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        root = self.makeBin(nums, 0, len(nums)-1)
        return root
        
        
        
    def makeBin(self, nums, low, high):
        if high < low:
            return None
        if high == low:
            root = TreeNode(nums[low])
            return root
        mid = (low + (high-low)/2)
        root = TreeNode(nums[mid])
        root.left = self.makeBin(nums, low, mid-1)
        root.right = self.makeBin(nums, mid+1, high)
        return root
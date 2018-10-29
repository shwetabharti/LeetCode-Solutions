class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return n
        res = [0 for i in range(0,n)]
        res[0] = 1; res[1] = 2
        for i in range(2,n):
            res[i] = res[i-1] + res[i-2]
        return res[n-1]
            
        
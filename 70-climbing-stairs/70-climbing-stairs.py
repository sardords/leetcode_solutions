class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2] 
        for i in range(n):
            new_el = res[-1] + res[-2]  
            res.append(new_el) 
        return res[n-1] 
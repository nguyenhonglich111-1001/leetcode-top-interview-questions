# NOTE Beats 100%
// Just like fibonnaci 
class Solution {
public:
    int climbStairs(int n) {
        
        if(n <= 2)
            return n;
        int prepre = 1;
        int pre = 2;
        int ans;
        
        for(int i = 3; i <= n; i++)
        {
            ans = prepre + pre;
            prepre = pre;
            pre = ans;
        }
        
        return ans;
    }
};
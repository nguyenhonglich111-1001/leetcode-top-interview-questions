# NOTE 99.13%
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> mp;
        
        int add1,add2;
        
        for(int i = 0; i < nums.size(); i++)
        {
            if(mp[target - nums[i]])
            {
                add2 = i + 1;
                add1 = mp[target - nums[i]];
                break;
            }
            else
            {
                mp[nums[i]] = i + 1;
            }
        }
        
        return {add1-1,add2-1};
    }
};
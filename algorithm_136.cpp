class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int, int> vMap;
        int res = 0;
        if(nums.empty())
            return NULL;
        for(int i = 0; i < nums.size(); i++)
        {
            vMap[nums[i]]++;
        }
        for(int i = 0; i < nums.size(); i++)
        {
            if(vMap[nums[i]] == 1)
            {
                res = nums[i];
                break;
            }
        }
        return res;
    }
};

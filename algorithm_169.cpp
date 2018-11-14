class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> hMap;
        for(int i = 0; i<nums.size(); i++)
        {
            hMap[nums[i]] = 0;
        }
        for(int i = 0; i<nums.size(); i++)
        {
            hMap[nums[i]] += 1;
            if(hMap[nums[i]] > nums.size()/2)
            {
                return nums[i];
                break;
            }
        }
    }
};

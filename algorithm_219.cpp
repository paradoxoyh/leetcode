class Solution {
public:
    int min(int A, int B)
    {
        return (A>B)?B:A;
    }
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> Map;
        if(!k) return false;
        for(int loop = 0; loop < nums.size(); loop++)
        {
            if(Map[nums[loop]]) return true;
            if(loop >= k) Map.erase(nums[loop - k]);
            Map[nums[loop]] = 1;
        }
        return false;
    }
};

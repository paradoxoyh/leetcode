class Solution {
public:
    void insert(vector<int>& vec, int num, int k)
    {
        if(num < vec[0]) return ;
        int i = 0;
        for(i = 1; i < k; i++)
        {
            if(num < vec[i]) break;
        }
        vec.insert(vec.begin()+i, num);
        vec.erase(vec.begin());
    }
    int findKthLargest(vector<int>& nums, int k) {
        vector<int> vec(k, -100);
        for(int loop = 0; loop < nums.size(); loop++)
        {
            insert(vec, nums[loop], k);
        }
        return vec[0];
    }
};

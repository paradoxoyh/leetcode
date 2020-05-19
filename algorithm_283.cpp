class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int res = 0;
        for(vector<int>::iterator it = nums.begin(); it != nums.end();)
        {
            if(it == nums.end()) break;
            if((*it) == 0) 
            {
                res++;
                nums.erase(it);
            }
            else it++;
        }
        for(int loop = 0; loop < res; loop++)
        {
            nums.push_back(0);
        }
    }
};

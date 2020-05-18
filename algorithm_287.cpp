class Solution {
public:
    void swap(int *A, int *B)
    {
        int tmp = *A;
        *A = *B;
        *B = tmp;
    }
    int findDuplicate(vector<int>& nums) {
        for(int loop = 0; loop < nums.size(); loop++)
        {
            while(true)
            {
                if(nums[loop] == loop) break;
                else if(nums[loop] == nums[nums[loop]]) return nums[loop];
                else
                {
                    swap(&nums[loop], &nums[nums[loop]]);
                }
            }
        }
        return 0;
    }
};

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res(0);
        if(!nums.size()) return res;
        int head = nums[0];
        int tail = nums[0];
        string str = "";
        for(int loop = 1; loop < nums.size(); loop ++)
        {
            if(nums[loop] == tail + 1) tail = nums[loop];
            else
            {
                str += to_string(head);
                if(tail > head)
                {
                    str += "->";
                    str += to_string(tail);
                }
                res.push_back(str);
                head = nums[loop];
                tail = nums[loop];
                str = "";
            }
        }
        str += to_string(head);
        if(tail > head)
        {
            str += "->";
            str += to_string(tail);
        }
        res.push_back(str);
        return res;
    }
};

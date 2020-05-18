class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1, 0);
        for(int loop = 1; loop <= num; loop++)
        {
            res[loop] = res[loop >> 1] + (1 & loop);
        }
        return res;
    }
};
/*
0111 = 0011 + 0111&1
0110 = 0011 + 0110&1
*/

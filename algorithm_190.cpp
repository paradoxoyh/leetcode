class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for(int loop = 0; loop < 32; loop++)
        {
            if(n%2)
            {
                res = (res << 1) + 1;
            }
            else
            {
                res = res << 1;
            }
            n = n >> 1;
        }
        return res;
    }
};

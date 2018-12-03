class Solution {
public:
    bool isUgly(int num) {
        num = subIsUgly(num, 2);
        num = subIsUgly(num, 3);
        num = subIsUgly(num, 5);
        return (num == 1)? true: false;
    }
    int subIsUgly(int num, int k){
        if(num > 0)
            while(true){
                if(num%k == 0)
                    num = num / k;
                else
                    break;
            }
        return num;
    }
};

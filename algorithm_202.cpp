class Solution {
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = n;
        while(true){
            fast = creatNewNum(fast);
            fast = creatNewNum(fast);
            slow = creatNewNum(slow);
            if(slow == 1)
                return true;
            else if(slow == fast)
                return false;
        }    
    }
    int creatNewNum(int n){
        int sum = 0;
        while(n >= 10){
            sum += pow(n%10, 2);
            n = n / 10;
        }
        sum += pow(n, 2);
        return sum;
    }
};

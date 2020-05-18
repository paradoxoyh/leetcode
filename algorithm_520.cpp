class Solution {
public:
    bool detectCapitalUse(string word) {
        int large = 0;
        int small = 0;
        for(int loop = 0; loop < word.size(); loop++)
        {
            if(word[loop] <= 'Z' && word[loop] >= 'A') large++;
            else small ++;
        }
        if(!small || !large) return true;
        else if(large == 1 && word[0] >= 'A' && word[0] <= 'Z') return true;
        else return false;
    }
};

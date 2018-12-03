class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> cMaps, cMapt;
        map<char, bool> bMaps, bMapt;
        for(int i = 0; i < s.size(); i++){
            if(bMaps[s[i]] && cMaps[s[i]] != t[i])
                return false;
            else
            {
                cMaps[s[i]] = t[i];
                bMaps[s[i]] = true;
            }
            if(bMapt[t[i]] && cMapt[t[i]] != s[i])
                return false;
            else
            {
                cMapt[t[i]] = s[i];
                bMapt[t[i]] = true;
            }
        }
        return true;
    }
};

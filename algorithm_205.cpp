class Solution {
public:
    bool isIsomorphic(string s, string t) {
        bool res;
        return subIsomorphic(s, t) && subIsomorphic(t, s);
    }
private:
    bool subIsomorphic(string s, string t){
        unordered_map<char, char> cMap;
        for(int i = 0; i < s.size(); i++){
            if(cMap.count(s[i]) == 0)
                cMap[s[i]] = t[i];
            else if(cMap[s[i]] != t[i])
                return false;
        }
        return true;
    }
};

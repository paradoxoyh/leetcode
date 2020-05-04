class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int N = citations.size();
        for(int i = 0; i < N; i++)
        {
            int curr = citations[N - 1 - i];
            if (curr == i + 1) return i + 1;
            if (curr < i + 1) return i;
        }
        return N;
    }
};

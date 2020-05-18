/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        queue<TreeNode *>Q;
        TreeNode *pTmp = NULL;
        int res = 0;
        if(root) Q.push(root);
        while(!Q.empty())
        {
            pTmp = Q.front();
            Q.pop();
            if(pTmp->left) Q.push(pTmp->left);
            if(pTmp->right) Q.push(pTmp->right);
            res++;
        }
        return res;
    }
};

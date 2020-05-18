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
    TreeNode* dfs(TreeNode *root, TreeNode *pNodeP, TreeNode *pNodeQ)
    {
        if((root->val > pNodeP->val) && (root->val > pNodeQ->val))
        {
            return dfs(root->left, pNodeP, pNodeQ);
        }
        else if((root->val < pNodeP->val) && (root->val < pNodeQ->val))
        {
            return dfs(root->right, pNodeP, pNodeQ);
        }
        return root;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* pRes = NULL;
        pRes = dfs(root, p, q);
        return pRes;
    }
};

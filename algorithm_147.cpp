/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* insert(struct ListNode *pHead, struct ListNode *pNode)
    {
        ListNode *pOne = pHead;
        ListNode *pTwo = NULL;
        while(pOne && (pNode->val > pOne->val))
        {
            pTwo = pOne;
            pOne = pOne->next;
        }
        pNode->next = pOne;
        if(pTwo) pTwo->next = pNode;
        return (pTwo)?pHead:pNode;
    }

    ListNode* insertionSortList(ListNode* head) {
        if(!head) return head;
        ListNode *pRes = head;
        ListNode *pNode = head->next;
        ListNode *pTmp = NULL;
        pRes->next = NULL;
        while(pNode)
        {
            pTmp = pNode->next;
            pRes = insert(pRes, pNode);
            pNode = pTmp;
        }
        return pRes;
    }
};

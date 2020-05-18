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
    void Switch(struct ListNode *pOne, struct ListNode *pTwo, struct ListNode *pTmp, struct ListNode *pPrev)
    {
        if(pPrev)
        {
            pPrev->next = pTwo;
        }
        pTwo->next = pOne;
        pOne->next = pTmp;
    }

    ListNode* swapPairs(ListNode* head) {
        ListNode *pOne = NULL;
        ListNode *pTwo = NULL;
        ListNode *pPrev = NULL;
        ListNode *pTmp = head;
        ListNode *pRes = head;
        if(!head)
        {
            return NULL;
        }
        pOne = pTmp;
        pTmp = pTmp->next;
        pTwo = pTmp;
        if(!pTmp)
            return pRes;
        pRes = pTwo;
        do
        {
            pTmp = pTmp->next;
            Switch(pOne, pTwo, pTmp, pPrev);

            pPrev = pOne;
            pOne = pTmp;
            if(!pTmp)
            {
                break;
            }
            pTmp = pTmp->next;
            pTwo = pTmp;
        }while(pTmp);
        return pRes;
    }

};

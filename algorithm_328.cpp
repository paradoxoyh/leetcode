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
    ListNode* oddEvenList(ListNode* head) {
        if(!head) return NULL;
        ListNode *pOdd = head;
        ListNode *pEven = head->next;
        ListNode *pFeven = head->next;
        while(pOdd && pEven)
        {
            pOdd->next = pEven->next;
            if(!pEven->next) break;
            pOdd = pEven->next;
            pEven->next = pOdd->next;
            pEven = pOdd->next;
        }
        pOdd->next = pFeven;
        return head;
    }
};

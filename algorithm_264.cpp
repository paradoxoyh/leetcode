class Solution {
public:
    typedef struct NODE
    {
        NODE *pNext;
        int long long val;
    }NODE;
    
    int nthUglyNumber(int n) {
        NODE *pHead = (NODE *)malloc(sizeof(NODE));
        NODE *p2 = (NODE *)malloc(sizeof(NODE));
        NODE *p3 = (NODE *)malloc(sizeof(NODE));
        NODE *p5 = (NODE *)malloc(sizeof(NODE));
        int res = 0;
        
        pHead->val = 1;
        pHead->pNext = p2;
        p2->val = 2;
        p2->pNext = p3;
        p3->val = 3;
        p3->pNext = p5;
        p5->val = 5;
        p5->pNext = NULL;
        while(n > 1)
        {
            NODE *pTmp = pHead;
            for(int i = 0; i < 3; i++)
            {
                int N = 0;
                unsigned int times = 0;
                NODE *pNode = (NODE *)malloc(sizeof(NODE));
                pNode->pNext = NULL;
                switch (i)
                {
                    case 0:
                    {
                        times = 2;
                        N = n;
                        break;
                    }
                    case 1:
                    {
                        times = 3;
                        break;
                    }
                    case 2:
                    {
                        times = 5;
                        break;
                    }
                }
                pNode->val = times * pHead->val;
                res = insertNode(pTmp, pNode, N);
                pTmp = pNode;
                if(res)
                    return res;
            }
            pHead = pHead->pNext;
            n--;
        }
        return pHead->val;
    }
    
    int insertNode(NODE *pHead, NODE *pNode, int Num)
    {
        int idx = 1;
        NODE *pTmp = pHead;
        NODE *pPrev = pHead;
        while(pTmp)
        {
            if(pNode->val > pTmp->val)
            {
                if(idx == Num)
                {
                    return pTmp->val;
                }
                pPrev = pTmp;
                pTmp = pTmp->pNext;
                idx++;
            }
            else if(pNode->val == pTmp->val)
            {
                pNode->pNext = pTmp;
                return 0;
            }
            else
                break;
        }
        pPrev->pNext = pNode;
        pNode->pNext = pTmp;
        return 0;
    }
};

struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *pre = NULL, *p = head, *next;
    if(head && head->next)
        head = head->next;
    while(p && p->next){
        next = p->next;
        if(pre)
            pre->next = next;
        p->next = next->next;
        next->next = p;
        pre = p;
        p = p->next;
    }
    return head;
}
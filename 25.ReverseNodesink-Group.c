struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    int i = 0;
    struct ListNode *p = head, *pre = NULL, *ret, *save;

    while(p){
        i++;
        p = p->next;
    }
    if(i < k)
        return head;

    for(i = 0, p = head; i < k - 1; i++)
        p = p->next;
    ret = p;
    p->next = reverseKGroup(p->next, k);
    pre = p->next;

    for(i = 0, p = head; i < k; i++){
        save = p->next;
        p->next = pre;
        pre = p;
        p = save;
    }

    return ret;
}
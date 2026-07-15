def deleteHead(head):
    #code here
    head.next.prev=None
    temp=head.next
    head.next=None
    head=temp
    return head
class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthFromEnd(self, head, n):    
    def delete(head):
        final = head
        pos =0
        if n == 1:
            head = head.next
            return head
        while head:
            pos+=1  
            if pos == n-1:
                node_after_next = head.next.next
                head.next = node_after_next
            head = head.next           
        return final

    def reverse(head):
        if head == None:
            return None
        if head.next==None:
            return head 
        last_seen = None
        while head:
            temp = head.next
            head.next = last_seen
            last_seen = head
            head = temp
            
        return last_seen
             
    return reverse(delete(reverse(head)))
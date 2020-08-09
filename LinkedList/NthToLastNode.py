class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def printAll(head):
    while head:
        print(head.data)
        head= head.next      
        
    """
 0->1->2->3->4
                ^
           ^    
 => 1->2->4

    """

def nthToLast(head, n=2):   
    dummy_head = ListNode(0)
    dummy_head.next = head
    fast = dummy_head
    slow = dummy_head
    
    for i in range(n):         
        if fast == None:
            break        
        fast = fast.next
                
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    
    return dummy_head.next 


LinkedList = Head(1)
LinkedList.next = Head(2)
LinkedList.next.next = Head(3)
LinkedList.next.next.next = Head(4)
LinkedList.next.next.next.next = Head(5)

print(nthToLast(LinkedList))

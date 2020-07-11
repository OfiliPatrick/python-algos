class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeLink(self, L1, L2):
    out = dummy = Node(0)
    while L1 and L2:
        if L1.val < L2.val:
            dummy.next, L1 = L1, L1.next
        else:
            dummy.next, L2 =   L2, L2.next        
        
        dummy = dummy.next

    if L1:
        dummy.next = L1
    else:
        dummy.next =  L2
    return out.next


LinkedList1 = Node(1)
LinkedList1.next = Node(5)
LinkedList1.next.next = Node(1)

LinkedList2 = Node(3)
LinkedList2.next = Node(11)

# print(LinkedList1.print(LinkedList1.mergeLink(LinkedList1,LinkedList2)))


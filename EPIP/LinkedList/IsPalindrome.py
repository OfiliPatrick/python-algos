class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def isPalindrome(self, L1):
    L1_list = []; L1_reverse = []
    dummy = L1
    while dummy:
        L1_list.append(dummy.val)
        dummy=dummy.next

    def rev(head):
        last_seen=None
        while head:
            nextt = head.next
            head.next = last_seen
            last_seen = head
            head = nextt
        return last_seen

    revL1 = rev(L1)
    while revL1:
        L1_reverse.append(revL1.val)
        revL1 = revL1.next 
    
    if L1_list == L1_reverse:
        return True
    else:
        return False
        
LinkedList1 = Node(1)
LinkedList1.next = Node(5)
LinkedList1.next.next = Node(1)

print(LinkedList1.isPalindrome(LinkedList1))
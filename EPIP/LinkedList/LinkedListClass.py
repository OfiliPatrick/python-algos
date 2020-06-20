class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def print(self, head):
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

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

LinkedList2 = Node(3)
LinkedList2.next = Node(11)

# print(LinkedList1.print(LinkedList1.mergeLink(LinkedList1,LinkedList2)))

print(LinkedList1.isPalindrome(LinkedList1))





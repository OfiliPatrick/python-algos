class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def printAll(self, head):
        while head:
            print(head.data)
            head= head.next      
        
LinkedList = Head(1)
LinkedList.next = Head(2)
LinkedList.next.next = Head(3)
LinkedList.next.next.next = Head(4)
LinkedList.next.next.next.next = Head(5)


LinkedList = Head(1)
LinkedList.next = Head(2)
LinkedList.next.next = Head(8)
LinkedList.next.next.next = Head(4)
LinkedList.next.next.next.next = Head(5)
arr = [1,2,3,4,5]
print(LinkedList.printAll(LinkedList.createLinkedFromList(arr)))





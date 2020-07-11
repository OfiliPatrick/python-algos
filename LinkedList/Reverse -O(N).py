class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def printAll(self, head):
        while head:
            print(head.data)
            head= head.next

def revIter(self, head):
    # Linear Space
    if head == None:
        return None
    if head.next == None:
        return head
    final = new_head = head
    my_list = []
    while head:
        my_list.append(head.data)
        head = head.next
    my_list.reverse()
    for i,num in enumerate(my_list):
        new_head.data = num
        if i ==len(my_list)-1:
            new_head.next= None
            break
        new_head = new_head.next

    return final
class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def revIter(self, head):
    # Constant Space
    if head == None:
        return None
    if head.next == None:
        return head
    final = new_head = head

    last_seen = None
    while head:
        nextt = head.next
        head.next = last_seen
        last_seen = head
        head = nextt


    return last_seen
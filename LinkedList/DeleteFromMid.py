class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def delFromMid(self, head):
    length = 0; new_head = head
    while head:
        length +=1
        head = head.next
    mid = (length // 2) + 1
    pos = 0
    while new_head:
        pos += 1
        if pos == mid:
            prev_node.next = new_head.next
        prev_node = new_head
        new_head = new_head.next

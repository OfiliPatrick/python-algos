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





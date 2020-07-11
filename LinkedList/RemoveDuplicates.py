class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDupliates(self, head):
    import collections
    seen = collections.defaultdict(bool)
    while head:
        if seen[head.data] == True:
            next_node = head.next
            last_seen.next = next_node
        else:
                last_seen = head
        seen[head.data] = True
        head = head.next

        
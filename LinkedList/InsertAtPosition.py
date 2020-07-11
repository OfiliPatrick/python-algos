class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtPosition(self, head, data, position):
    new_Node = Head(data)
    if position == 0 or head == None:
        head = new_Node
    if position == 1:
        head.next = new_Node
    pos = -1 
    while head :
        pos +=1
        if pos == position -1:
            head.next , new_Node.next = new_Node, head.next
        head = head.next
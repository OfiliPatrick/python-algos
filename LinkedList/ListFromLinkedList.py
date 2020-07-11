class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedFromList(self,list_vals):
        final_list = start_head = Head(list_vals[0])
        for i in range(1, len(list_vals)):
            val = list_vals[i]
            new_node = Head(val)
            start_head.next = new_node
            start_head = start_head.next
        return final_list

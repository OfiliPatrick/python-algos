class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def search(self, LinkedList, key):
        while LinkedList != None:
            if LinkedList.data == key:
                return key, "is present"
            LinkedList = LinkedList.next

        return key, 'is not present'
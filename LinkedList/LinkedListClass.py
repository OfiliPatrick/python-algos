class Head(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def printAll(self, head):
        while head:
            print(head.data)
            head= head.next

    def search(self, LinkedList, key):
        while LinkedList != None:
            if LinkedList.data == key:
                return key, "is present"
            LinkedList = LinkedList.next

        return key, 'is not present'

    def insert(self, node, newNode):
        node_after = node.next
        node.next, newNode.next = newNode, node_after
        
    def delete(self, node):
        node.next = node.next.next
    
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
      
    def cycleCheck(self, head):
        tort = head
        
        pass

    def removeNthFromEnd(self, head, n):    
        def delete(head):
            final = head
            pos =0
            if n == 1:
                head = head.next
                return head
            while head:
                pos+=1  
                if pos == n-1:
                    node_after_next = head.next.next
                    head.next = node_after_next
                head = head.next           
            return final
        
        def reverse(head):
            if head == None:
                return None
            if head.next==None:
                return head 
            last_seen = None
            while head:
                temp = head.next
                head.next = last_seen
                last_seen = head
                head = temp
                
            return last_seen
                
           
        return reverse(delete(reverse(head)))
        
    def createLinkedFromList(self,list_vals):
        final_list = start_head = Head(list_vals[0])
        for i in range(1, len(list_vals)):
            val = list_vals[i]
            new_node = Head(val)
            start_head.next = new_node
            start_head = start_head.next
        return final_list

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





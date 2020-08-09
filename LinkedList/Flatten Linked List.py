def flatten(head):
    stack = []
    new_head = head
    
    while head:
        if head.child:
            if head.next:
                stack.append(head.next)
            head.next = head.child
            head.next.prev = head
            head.child = None
        
        if head.next == None and stack:
            curr_node = stack.pop()
            head.next = curr_node
            head.next.prev = head
    
        head = head.next

          
    return new_head
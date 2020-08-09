def flatten(root):
  
  if root == None:
      return None
  
  stack = [root]
  
  while stack:
      curr_node = stack.pop()
      
      if curr_node.right:
          stack.append(curr_node.right)
          
      if curr_node.left:
          stack.append(curr_node.left)
      
      if stack:
          curr_node.right = stack[-1]
      
      curr_node.left = None
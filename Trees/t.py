#  def isUnivalTree(self, root: TreeNode) -> bool:
#         import collections
#         seen = collections.defaultdict(bool)
#         def helper(root):
#             if root == None:
#                 return True
            
#             if seen[root.val] == True:
#                 return False
            
#             seen[root.val] =  True
#             left =  helper(root.left)
#             right = helper(root.right)
            
#             if left == False:
#                 return right
#             return left
        
#         return helper(root)
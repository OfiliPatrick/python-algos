# All iters
def rev1(s):
    return s[::-1]

def rev2(s):
    return "".join(list(reversed(s)))


def rev3(s):
    list_s = list(s)
    max_index = len(list_s)-1
    for i in range(0, (max_index//2)+1):
        list_s[i], list_s[max_index - i] = list_s[max_index - i], list_s[i]
    return "".join(list_s)

# two pointers
def rev4(s):
    list_s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        list_s[left], list_s[right] = list_s[right], list_s[left]
        left += 1
        right-=1

    return  "".join(list_s) 

#Recursive solutions
def rev5(s):
    if len(s) <= 1:
        return s
    return rev5(s[1:]) + s[0]
    

def rev6(s):
    if len(s) == 1:
        return s
    return s[-1] + rev6(s[:-1])



print(rev6('this is good'))





# print "Practice makes Perfect!"   

# #https://leetcode.com/problems/search-insert-position/
  
  
# arr = [1,3,5,6]
# target = 0

# def search(arr,target):
#   import collections
#   my_dict = collections.defaultdict(int)  
#   for num in arr:
#     my_dict[num]+=1
        
#   if my_dict[target] ==0 and target > max(arr):
#     return len(arr)
     
#   if my_dict[target] ==0 and target < min(arr):
#     return 0
  
#   for i,num in enumerate(arr):
#     if i+1 < len(arr):
#       if num  == target:
#         return i
#         break
#       if num < target and arr[i+1] > target:
#         return i +1
#       if i == len(arr) - 1 and target > arr[len(arr)-1]:
#         return i+1
    
# print(search(arr,target))
    
  
    
    
    


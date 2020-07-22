def isValid(self, s: str) -> bool:
    if s == '':
        return True
    if s[0] == '}' or s[0] == ']' or s[0] == ')':
        return False
    my_stack = []
    for i in range(len(s)):
        char = s[i]
        if char == '{' or char == '[' or char == '(':
            my_stack.append(char)
        if char == ')':
            # A balanced sub bracket must start with an opening
            if len(my_stack) == 0:
                return False
            last = my_stack[-1]
            if last == '(':
                my_stack.pop()
            else:
                return False
        elif char == ']':
            if len(my_stack) == 0:
                return False
            last = my_stack[-1]
            if last == '[':
                my_stack.pop()
            else:
                return False
        elif char == '}':
            if len(my_stack) == 0:
                return False
            last = my_stack[-1]
            if last == '{':
                my_stack.pop() 
            else:
                return False

    if len(my_stack) ==0:
        return True
    else:
        return False
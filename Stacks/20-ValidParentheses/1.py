## It does not work

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in s:
            stack.append(i)

        p = 0
        for i in reversed(stack):

            if p == 0:
                if i == ')':
                    p = 1
                    stack.pop()
                else:
                    if i == ']':
                        p = 2
                        stack.pop()
                    else:
                        if i == '}':
                            p = 3
                            stack.pop()
                        else:
                                return False
            else:
                if (p == 1) and (i == '('):
                    stack.pop()
                    p = 0
                    continue
                else: 
                    if p == 2 and (i == '['):
                        stack.pop()
                        p = 0
                        continue
                    else:
                        if p == 3 and (i == '{'):
                            stack.pop()
                            p = 0
                            continue
                        else:
                            return False


        return True
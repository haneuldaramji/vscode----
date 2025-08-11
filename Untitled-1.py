import sys
stack =[]
def push (item):
    """Push an item onto the stack."""
    stack.append(item)
    return(item)

def pop ():
    """Pop an item off the stack."""
    if not stack:
        return -1
    return stack.pop()

def size():
    """Return the number of items in the stack."""
    return len(stack)   

def empty():
    """Check if the stack is empty."""
    return len(stack) == 0 

def top():
        """Return the top item of the stack without removing it. If empty, return -1."""
        if not stack:
            return -1
        return stack[-1]

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == "push":
        print(push(int(cmd[1])))
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "top":
        print(top())

def push(item):
    queue.append(item)

def pop():
    if not queue:
        return -1
    return queue.pop(0)

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    return 0

def front():
    if not queue:
        return -1
    return queue[0]

def back():
    if not queue:
        return -1   
    return queue[-1]

import sys
n = int(sys.stdin.readline())
queue = []
for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "front":
        print(front())
    elif cmd[0] == "back":
        print(back())
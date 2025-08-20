#deque 구현
deque = []

def push_front(X):
# 정수 X를 덱의 앞에 추가
    deque.insert(0, X)

def push_back(X):
# 정수 X를 덱의 뒤에 추가
    deque.append(X)

def pop_front():
# 덱의 앞에서 정수를 제거하고 그 값을 반환
    if not deque:
        return -1
    return deque.pop(0)

def pop_back():
# 덱의 뒤에서 정수를 제거하고 그 값을 반환
    if not deque:
        return -1
    return deque.pop()

def size():
# 덱에 들어있는 정수의 개수를 반환
    return len(deque) 

def empty():
# 덱이 비어있으면 1, 아니면 0을 반환
    return 1 if not deque else 0

def front():
# 덱의 가장 앞에 있는 정수를 반환
    if not deque:
        return -1
    return deque[0] 

def back():
# 덱의 가장 뒤에 있는 정수를 반환
    if not deque:
        return -1
    return deque[-1]

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push_front":
        push_front(int(command[1]))
    
    elif command[0] == "push_back":
        push_back(int(command[1]))
    
    elif command[0] == "pop_front":
        print(pop_front())
    
    elif command[0] == "pop_back":
        print(pop_back())
    
    elif command[0] == "size":
        print(size())

    elif command[0] == "empty":
        print(empty())
    
    elif command[0] == "front":
        print(front())
    
    elif command[0] == "back":
        print(back())


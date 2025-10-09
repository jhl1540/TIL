# Matrices and Operations
# https://school.programmers.co.kr/learn/courses/30/lessons/118670

from collections import deque

def solution(rc, operations):

    R, C = len(rc), len(rc[0])


    left_col  = deque(row[0] for row in rc)
    right_col = deque(row[-1] for row in rc)
    middles   = deque(deque(row[1:-1]) for row in rc)



    def shift_row():
        left_col.rotate(1)
        right_col.rotate(1)
        middles.rotate(1)

    def rotate():
        if C == 2:
            right_col.appendleft(left_col.popleft()) 
            left_col.append(right_col.pop())          
        else:
            middles[0].appendleft(left_col.popleft())
            right_col.appendleft(middles[0].pop())
            middles[-1].append(right_col.pop())
            left_col.append(middles[-1].popleft())

    for op in operations:
        if op == "ShiftRow":
            shift_row()
        else:  
            rotate()


    L = list(left_col)
    Rr = list(right_col)
    M = [list(m) for m in middles]  

    result = []
    if C == 2:
        for i in range(R):
            result.append([L[i], Rr[i]])
    else:
        for i in range(R):
            result.append([L[i]] + M[i] + [Rr[i]])

    return result

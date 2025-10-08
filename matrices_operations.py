# Matrices and Operations
# https://school.programmers.co.kr/learn/courses/30/lessons/118670

from collections import deque

def solution(rc, operations):
    # Get the number of rows and columns
    R, C = len(rc), len(rc[0])

    # --- Step 1: Decompose the matrix into three parts ---
    # left_col  : deque of all first-column elements (top to bottom)
    # right_col : deque of all last-column elements (top to bottom)
    # middles   : deque of deques, each holding the middle elements of each row
    left_col  = deque(row[0] for row in rc)
    right_col = deque(row[-1] for row in rc)
    middles   = deque(deque(row[1:-1]) for row in rc)

    # --- Step 2: Define helper functions for the two operations ---

    def shift_row():
        """
        Shifts all rows downward by one.
        The last row becomes the first row.
        This means rotating all three deques together.
        """
        left_col.rotate(1)
        right_col.rotate(1)
        middles.rotate(1)

    def rotate():
        """
        Rotates the outer border of the matrix clockwise by one position.
        Operates on the top row, bottom row, left column, and right column simultaneously.
        """
        if C == 2:
            # Special case: if there are only two columns, there are no middle elements
            # So just rotate the left and right columns directly
            right_col.appendleft(left_col.popleft())  # top-right <= top-left
            left_col.append(right_col.pop())          # bottom-left <= bottom-right
        else:
            # 1) Move top-left element to top-middle
            middles[0].appendleft(left_col.popleft())
            # 2) Move top-middle (rightmost of top row) to top-right
            right_col.appendleft(middles[0].pop())
            # 3) Move bottom-right to bottom-middle
            middles[-1].append(right_col.pop())
            # 4) Move bottom-middle (leftmost of bottom row) to bottom-left
            left_col.append(middles[-1].popleft())

    # --- Step 3: Apply all operations in order ---
    for op in operations:
        if op == "ShiftRow":
            shift_row()
        else:  # "Rotate"
            rotate()

    # --- Step 4: Rebuild the final 2D matrix from the three parts ---
    L = list(left_col)
    Rr = list(right_col)
    M = [list(m) for m in middles]  # Convert inner deques to lists

    result = []
    if C == 2:
        # No middle elements; only two columns
        for i in range(R):
            result.append([L[i], Rr[i]])
    else:
        # Combine left + middle + right for each row
        for i in range(R):
            result.append([L[i]] + M[i] + [Rr[i]])

    return result

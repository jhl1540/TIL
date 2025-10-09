
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders, course):
    orders = [''.join(sorted(o)) for o in orders]
    answer = []

    for k in course:
        counter = Counter()
        for o in orders:
            if len(o) < k:
                continue
            # Count every k-combination from this order
            counter.update(''.join(c) for c in combinations(o, k))

        if not counter:
            continue

        # Only consider combos that appear at least twice
        max_cnt = max(counter.values(), default=0)
        if max_cnt < 2:
            continue

        # Collect all combos with the max count for this course size
        answer += [menu for menu, cnt in counter.items() if cnt == max_cnt]

    return sorted(answer)

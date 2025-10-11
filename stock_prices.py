# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):
        val = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                val += 1
            else:
                val += 1
                break
        answer.append(val)
    return answer

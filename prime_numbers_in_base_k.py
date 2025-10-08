# Finding the number of prime numbers in base k
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    
    n_list = []
    max_exp = 0
    while True:
        if n - k ** max_exp >= 0:
            max_exp += 1
        else:
            break

    e = max_exp
    N = n 
    for i in range(max_exp):
        cur_exp = max_exp - 1 - i
        digit = N // k ** cur_exp
        N -= digit * (k ** cur_exp)
        n_list.append(str(digit))
    conv_n = [int(s) for s in ''.join(n_list).split('0') if s.strip()]
    
    nums = 0
    t_list = []
    for elem in conv_n:
        t_val = 1
        if elem == 1:
            t_val = 0
        elif elem in (2, 3):
            t_val = 1
        else:
            for j in range(2, int(elem**0.5) + 1):
                if elem % j == 0:
                    t_val = 0
                    break
        t_list.append(t_val)
        
    answer = sum(t_list)
    return answer 



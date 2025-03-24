import random
import math

def generate_permutation(n):
    l = [i for i in range(n)]
    m = n
    k = []
    for i in range(m):
        j = random.randint(0, m - 1)
        k += [l[j]]
        temp = l[j]
        l[j] = l[-1]
        l[-1] = temp
        m -= 1
        l = l[:m]
    return k

def avg_times_max_gets_updated(n, N):
    sum = 0
    for i in range(N):
        l = generate_permutation(n)
        count = 0
        max = -math.inf
        for j in range(n):
            if max < l[j]:
                max = l[j]
                count += 1
        sum += count    
    return sum / N

def good_permutation(l):
    for i in range(len(l)):
        if l[i] == i:
            return False
    return True

def avg_times_chosen_permutation_is_good(n, N):
    count = 0
    for i in range(N):  
        l = generate_permutation(n)
        if good_permutation(l):
            count += 1
    return N / count

# t = generate_permutation(5)
print(avg_times_max_gets_updated(149, 10000))
print(avg_times_chosen_permutation_is_good(10, 10000))

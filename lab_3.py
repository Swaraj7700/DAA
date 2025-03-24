def josephus_circ(l, ind, k):
    if len(l) == 1:
        print(l[0])
        return
    ind = (ind + k) % len(l)
    l.pop(ind)
    josephus_circ(l, ind, k)
    
def josephus_norm(l, k):
    while(len(l) > 1):
        for i in range(len(l)):
            if i % k == 0:
                l.pop(i)
    print(l[0])
    
n = int(input("Enter the number of people : "))
l = [i for i in range(1, n + 1)]
josephus_circ(l, 0, 1)
josephus_norm(l, 2)
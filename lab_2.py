class Node():
    def _init_(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
        
def quicksort_bst(l):
    root = Node(l[0])
    for i in range(1, len(l)):
        insert(root, l[i])
    inorder(root)

def partition(L, lower, upper):
    pivot = L[lower]
    i = lower
    for j in range(lower + 1, upper + 1):
        if L[j] <= pivot:
            i += 1
            L[j], L[i] = L[i], L[j]
    L[lower], L[i] = L[i], L[lower]
    return i    

def quicksort(L, lower, upper):
    if lower < upper:
        pivot_pos = partition(L, lower, upper)
        quicksort(L,lower,pivot_pos-1)
        quicksort(L,pivot_pos+1,upper)
    return L
    
def merge(A, B):
    m, n = len(A), len(B)
    C, i, j = [], 0, 0
    
    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            
    while i < m:
        C.append(A[i])
        i += 1
    
    while j < n:
        C.append(B[j])
        j += 1
        
    return C

def mergesort(l):
    n = len(l)
    if n <= 1:
        return l
    m = n // 2
    left = mergesort(l[:m])
    right = mergesort(l[m:])
    sorted = merge(left, right)
    return sorted

def k_way_merge_sort(L, k):
    if len(L) <= 1:
        return L

    sublists = [L[i::k] for i in range(k)]

    sorted_sublists = [mergesort(sublist) for sublist in sublists]

    while len(sorted_sublists) > 1:
        merged_sublists = []
        for i in range(0, len(sorted_sublists), 2):
            if i + 1 < len(sorted_sublists):
                merged_sublists.append(merge(sorted_sublists[i], sorted_sublists[i + 1]))
            else:
                merged_sublists.append(sorted_sublists[i])
        sorted_sublists = merged_sublists

    return sorted_sublists[0] if sorted_sublists else []

l = [7, 5, 3, 10, 8, 2, 9]
k = 3  
print(k_way_merge_sort(l, k))
    
l = [7, 5, 3, 10, 8, 2, 9]
quicksort_bst(l)
print(quicksort(l,0,len(l)-2))
print(mergesort(l))

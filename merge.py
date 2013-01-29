def merge(L1, L2):
    i = 0
    j = 0
    res = []
    while i < len(L1) or j < len(L2):
        if i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                res.append(L1[i])
                i += 1
            else:
                res.append(L2[j])
                j += 1
        elif i < len(L1):
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1
    return res

def mergeSort(L):
    n = len(L)
    if n <= 1:
        return L
    L1 = L[:n/2]
    L2 = L[n/2:]

    left = mergeSort(L1)
    right = mergeSort(L2)
    return merge(left, right)


if __name__ == '__main__':
    L = [4,1,8,9,6,1,4,2,7,9,0,6,8,3,2,7,8,4]
    print mergeSort(L)

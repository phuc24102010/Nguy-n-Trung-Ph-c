def gt(n):
    if n==0:
        return 1
    return n*gt(n-1)
x=int(input())
print(gt(x))
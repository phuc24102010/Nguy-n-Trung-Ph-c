n=int(input())
d=0
while n>0:
    d+=(n%10)
    n//=10
print(d)
n=int(input())
k=int(input())
n= (n & ~(1<<k))
print(n)
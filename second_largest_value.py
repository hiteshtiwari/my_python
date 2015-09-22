#Second largest value..
#method one
N=raw_input()
A=map(int, raw_input().strip().split(" "))
A=sorted(set(A))
print A[-2]

#method 2

i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)
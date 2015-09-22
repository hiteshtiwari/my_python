M=int(raw_input())
L1=list(map(int, raw_input().strip().split(" ")))
N=int(raw_input())
L2=list(map(int, raw_input().strip().split(" ")))
S1=set()
S2=set()
S3=set()
S4=set()
S1.update(L1)
S2.update(L2)
S3=S1.union(S2)
S4=S1.intersection(S2)
S1=S3.difference(S4)

L=list(S1)
for i in sorted(L):
    print i
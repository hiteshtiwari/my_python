# List question as per user input insert/update/remove/pop query work

N=int(input())

for t in range(N):
    ar = raw_input().strip().split(" ")
    if ar[0] == "append":
        L.append(int(ar[1]))
    elif ar[0] == "insert":
        L.insert(int(ar[1]), int(ar[2]))
    elif ar[0] == "remove":
        L.remove(int(ar[1]))
    elif ar[0] == "pop":
        L.pop()
    elif ar[0] == "sort":
        L.sort()
    elif ar[0] == "reverse":
        L.reverse()
    elif ar[0] == "print":
        print L

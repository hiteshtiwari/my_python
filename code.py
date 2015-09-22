# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())
sub_list=[]
full_list=[]
if N>0 and N<6:
    for i in range(N):
        for i in range(2):            
            sub_list.append(raw_input())
        if len(sub_list) == 2:
            full_list.append(sub_list)
            sub_list = []
        if sub_list:
            full_list.append(sub_list)
    if type(full_list[0][0]) is int or type(full_list[0][0]) is float:
        full_list.sort()
        values=full_list[0][0]
        count = 1
        while count < N:
            for i in range(1,N):
                if full_list[0][0] in full_list[i]:
                    count += 1
                    values.append(full_list[i+1][1])
                    values.sort()
            for i in values:
                print i
    else:
        #full_list.sort()
        #full_list.sort(key = itemgetter(1), reverse = True)
        sorted(full_list, key = lambda x: int(x[1]))
        values=full_list[0][0]
        count = 1
        while count < N:
            for i in range(1,N):
                if full_list[0][0] in full_list[i]:
                    count += 1
                    values.append(full_list[i][0])
                    values.sort()
            for i in values:
                print i 
        
        
    
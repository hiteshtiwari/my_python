# Enter your code here. Read input from STDIN. Print output to STDOUT
str1=raw_input()
str2=raw_input()
count = 0
for i in range(len(str1)):
    if str2 == str1[i:i+len(str2)]:
        count += 1
print count    
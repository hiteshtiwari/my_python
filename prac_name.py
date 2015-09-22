"""
Problem Statement

Let's learn the basics of Python! You are given the first name and the last name of a person. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
It's that simple!

In Python you can read a line as a string using

s = raw_input()
#here s reads the whole line.  
Input Format The first line contains the first name, and the second line contains the last name.

Constraints 
The length of the first and last name ≤ 10.

Output Format Print the output as mentioned above.

Sample Input

Guido
Rossum
Sample Output

Hello Guido Rossum! You just delved into python.
"""

first_name = raw_input()
if len(first_name) in range(1,11):
    last_name = raw_input()
    if len(last_name) in  range(1,11):
        print "Hello %s %s! You just delved into python." % (first_name, last_name)
    else:
        exit()
else:
    exit()
    
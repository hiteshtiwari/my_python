"""Problem Statement

Let's learn about Python's arithmetic operators.

First, let's read two integers:

a = int(raw_input())
b = int(raw_input())
Now, the three basic arithmetic operators are the following:

Addition (+)
Subtraction (-)
Multiplication (*)
(We'll learn about division in the next task)

Task 
Read two integers from STDIN and print three lines where: 
(1) the first line contains the sum of the two numbers, 
(2) the second line contains the difference of the two numbers (first - second), 
(3) the third line contains the product of the two numbers.

Input Format 
The first line contains the first integer, a, and the second line contains the second integer, b.

Constraints 
1≤a≤109 
1≤b≤109

Output Format 
Print three lines as explained above.

Sample Input

3
2
Sample Output

5
1
6
Explanation 
3+2⟹5 
3−2⟹1 
3∗2⟹6

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = int(raw_input())
if a in range(1, 10000001):
    b = int(raw_input())
    if b  in range(1, 10000001):
        print a + b
        print a - b 
        print a * b
    else:
        print "give th ecorrect value  of b"
        exit()
else:
    print "give the value of a  in range"
    exit()
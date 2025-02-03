import sys
import re
S = sys.stdin.readline().strip()

num = re.findall(r'\d+',S)
opper = [x for x in S if not x.isdigit()]


i=0
while '+' in opper:
    if opper[i] == '+':
        num[i] =  int(num[i]) + int(num[i+1])
        opper.pop(i)
        num.pop(i+1)
        i=0
    else:    
        i += 1

i=0
while '-' in opper:
    if opper[i] == '-':
        num[i] =  int(num[i]) - int(num[i+1]) 
        opper.pop(i)
        num.pop(i+1)
        i = 0
    else:
        i += 1

print(num[0])

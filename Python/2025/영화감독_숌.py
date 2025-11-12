N = int(input())
num = 0
result = []
count = 0 
while True:
    num +=1
    if '666' in str(num):
        #result.append(num)
        count +=1
        if count == N:
            print(num)
            break

#print(result[N-1])
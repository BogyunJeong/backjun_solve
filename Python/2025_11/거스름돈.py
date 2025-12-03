N = int(input())

amount = 1000 - N

lst = [500,100,50,10,5,1]

result = 0
for i in lst:
    result += (amount // i)
    amount = amount % i

print(result)
imos = [0,1,1,1,0,0,0,0,-2,0,0,-1]
now = 0
for i in range(12):
   now += imos[i]
   imos[i] = now

print(imos)
a = [[1,2,3],[4,5,6],[7,8,9]]
sumR = [0]*3
sumC = [0]*3
sum=0
for posi,i in enumerate(a):
    for posj,j in enumerate(i):
        sumR[posi]=sumR[posi]+j
        sumC[posj]=sumC[posj]+j
        sum+=j
avg = sum/9
print(avg)
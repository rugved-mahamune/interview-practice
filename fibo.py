'''def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = 8
print(fibonacci(num))'''

list1 = [0,1]
n = 8
curr = 2
while(curr < n):
    list1.append(list1[curr-1] + list1[curr-2])
    curr+=1
print(list1)
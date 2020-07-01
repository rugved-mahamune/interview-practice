def num_coins(cents):
    if cents < 1:
        return 0
    coins = [25, 10, 5 ,1]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += cents/coin
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins

print(num_coins(31))

def my_num_coins(totalS):
    coins = [25, 10, 5 ,1]
    coins_total = 0
    for i in coins:
        if(totalS/i >= 1):
            coins_total += int(totalS/i)
            totalS = totalS%i
    return coins_total
            
print(my_num_coins(31))
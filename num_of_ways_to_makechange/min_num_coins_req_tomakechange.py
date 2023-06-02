# Find min number of coins to make amount
# We can use asmany coins as possible

amount = 6
coins = [1, 2, 4]


def get_min_coins(coins, amount):
    ways = [0 for x in range(amount)]
    ways[0] = 1

    for coin in coins:
        for amt in range(amount):
            if coin <= amt:
                ways[amt] = min(ways[amt], ways[amt - coin])
    return ways[-1]

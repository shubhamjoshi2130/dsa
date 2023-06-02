# Given a $ ammount and an array of numbers (integer coin denomination)
# We can use as many coins as we want.
# Question is to find all number if combinations that sum up to 10


def get_ways(array, n):
    """dynamic botton up
    """
    ways = [0 for x in range(n + 1)]

    ways[0] = 1

    for n in array:
        for amount in range(1, n + 1):
            if n <= amount:
                ways[amount] += ways[amount - n]
    return ways[n]


# Try this later
# def get_ways_rec(array,n):
#     return get_ways_rec_helper(array,n)

# def get_ways_rec_helper(array,n):
#     """dynamic top down
#     """
#     if n==0:
#         return 1
#     else:
#         return max(get_ways_rec_helper(array,n),get_ways_rec_helper(array,n) + )


def get_min_coins(coins,n):
    ways = [0 for x in range(n + 1)]
    
    for i in range(len(ways)):
        for j in range(len(coins)):
            ways[i] = min(ways[i],)
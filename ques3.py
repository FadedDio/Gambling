
def func(x, p):
    return x*p/(1-p)+1

def game_duration(p, q, k, t, W):
    """
    Return the expected number of rounds the gambler will play before quitting.

    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    t : int, t < k, the gambler will quit if she reaches t
    W : int, the threshold on maximum wealth the gambler can reach
    # """
    x = p + 1
    for i in range(W-1):
        x = func(x, p)
    return x*(k-t)/(1-p)

# # Example parameters
# p = 0.6
# q = 1 - p
# k = 150
# t = 100
# W = 100

# # Calculate expected rounds
# expected_rounds_result = game_duration(p, q, k, t, W)
# print("Expected number of rounds:", expected_rounds_result)

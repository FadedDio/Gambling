def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if (N==0):
        return 0
    elif (N==1):
        return k
    r = q/p
    if p != q:
        return (1 - r**k)/(1 - r**N)
    return k/N

def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if q < p:
        return 1 - (q/p)**k
    return 0

def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    r = q/p
    if p != q:
        return k/(q-p)+ N/(p-q)*(1 - r**k)/(1 - r**N)
    return -k**2 + k*N

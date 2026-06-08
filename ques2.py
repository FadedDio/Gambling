import math
"""
Use the following function to convert the decimal fraction of k/N into it's binary representation
using k_prec number of bits after the decimal point. You may assume that the expansion of 
k/N terminates before k_prec bits after the decimal point.
"""
def decimalToBinary(num, k_prec): 
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral 
   
    while (Integral):       
        rem = Integral % 2
        binary += str(rem)  
        Integral //= 2

    binary = binary[::-1]  # Reverse the string
    binary += '.'

    while k_prec: 
        fractional *= 2
        fract_bit = int(fractional)  
        if fract_bit == 1:  
            fractional -= fract_bit  
            binary += '1'       
        else: 
            binary += '0'
        k_prec -= 1
        
    return binary 

def win_probability(p, q, k, N):
    """
    Return the probability of winning while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if k == 0:
        return 0    
    elif k == N:
        return 1
    k_prec = math.ceil(math.log(N, 2)) + 100
    str = decimalToBinary(k / N, k_prec)
    while str[-1] == '0':
        str = str[:-1]
    str = str.split('.')
    str = str[1]
    def dp(str, i, p, q):
        if i == len(str):
            return 0
        if str[i] == '1':
            return q*dp(str, i+1, p, q) + p
        else:
            return p*dp(str, i+1, p, q) 
    return dp(str, 0, p, q)


def game_duration(p, q, k, N, cache=None):
    """
    Return the expected number of rounds to either win or get ruined while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if k == 0:
        return 0    
    elif k == N:
        return 0
    k_prec = math.ceil(math.log(N, 2)) + 100
    str = decimalToBinary(k / N, k_prec)
    while str[-1] == '0':
        str = str[:-1]
    str = str.split('.')
    str = str[1]
    def dp(str, i, p, q):
        if i == len(str):
            return 0
        if str[i] == '1':
            return 1 + q*dp(str, i+1, p, q) 
        else:
            return 1 + p*dp(str, i+1, p, q) 
    return dp(str, 0, p, q)
# # Example input values
# p = 0.6
# q = 1 - p  # Calculate q
# k = 50
# N = 100

# probability = win_probability(p, q, k, N)
# game_duration = game_duration(p, q, k, N)
# print(f"Probability of winning the game starting with initial wealth k = {probability}")
# print(f"Expected number of rounds to either win or get ruined starting with initial wealth k = {game_duration}")
import numpy as np
def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    
    """
    arr = [0]*(N+1)
    arr[0] = 1
    for i in range(1, N+1):
        arr[i] = arr[i-1]*(p[i-1]/q[i])
    # arr looks like [1, p[0]/q[1], p[0]*p[1]/q[1]q[2], p[0]*p[1]*p[2]/q[1]q[2]q[3], ...]
    # Normalize the array
    sum = 0
    for i in range(N+1):
        sum += arr[i]
    normalize = 1/sum
    for i in range(N+1):
        arr[i] *= normalize
    return arr

def expected_wealth(p, q, r, N):
    """
    Return the expected wealth of the gambler in the long run.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """
    sum = 0
    for i in range(N+1):    
        sum+=i*stationary_distribution(p, q, r, N)[i]
    return sum

def expected_time(p, q, r, N, a, b):
    """
    Returns the expected time to reach state b from state a.

    p : array of size N+1, probability of price increase
    q : array of size N+1, probability of price decrease
    r : array of size N+1, probability of price remaining the same
    N : int, the maximum price of the stock
    a : int, the starting price
    b : int, the target price
    """
    if a == b:
        return 0.0

    # Create the coefficient matrix A of size (N+1)x(N+1)
    A = np.zeros((N + 1, N + 1))
    rhs = np.ones(N + 1)  # Right-hand side for the equations
    rhs[b] = 0  # Expected time to reach target state b is 0
    # A(N + 1, N+1)E(N + 1, 1) = rhs(N + 1, 1)
    for i in range(N + 1):
        A[i, i] = 1 - r[i]  # Main diagonal
        if i > 0:
            A[i - 1, i] = -p[i - 1]  # Lower diagonal
        if i <= N - 1:
            A[i + 1, i] = -q[i + 1]  # Upper diagonal
    for i in range(N + 1):
        if i == b:
           A[b][i] = 1
        else:
            A[b][i] = 0
    
    # Solve for E
    E = np.linalg.solve(A, rhs)
    return E[a]  # Expected time from state a to reach target state b

# # Example usage
# N = 3  # Maximum number of states
# p = [0.5, 0.25, 0.25, 0]
# q = [0, 0.25, 0.25, 0.5]
# r = [0.5] * (N + 1)  # Probability of staying in the same state

# a = 1  # Starting state
# b = 2  # Target state

# print("Stationary distribution:", stationary_distribution(p, q, r, N))
# print("Expected wealth in the long run:", expected_wealth(p, q, r, N))
# print("Expected time from state", a, "to reach state", b, "is:", expected_time(p, q, r, N, a, b))

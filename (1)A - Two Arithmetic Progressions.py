import sys
from math import gcd
def get_divisors(n):
    """Get all divisors of n"""
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
        i += 1
    return sorted(divs)
def count_multiples(a, b, m, n):
    """Count i in [1,n] where ai+b ≡ 0 (mod m)"""
    if a == 0:
        return n if b % m == 0 else 0
    g = gcd(a, m)
    if b % g != 0:
        return 0
    # Solve (a/g)*i ≡ -(b/g) (mod m/g)
    m_prime = m // g
    a_prime = a // g
    b_prime = (-b // g) % m_prime
    # Modular inverse using extended Euclidean
    def extended_gcd(x, y):
        if x == 0:
            return y, 0, 1
        g, p1, p2 = extended_gcd(y % x, x)
        return g, p2 - (y // x) * p1, p1
    _, inv, _ = extended_gcd(a_prime % m_prime, m_prime)
    inv = inv % m_prime
    # First solution
    i0 = (b_prime * inv) % m_prime
    if i0 == 0:
        i0 = m_prime
    # Count solutions in [1, n]
    if i0 > n:
        return 0
    return (n - i0) // m_prime + 1
def solve_one(N, A, B, C, D):
    MOD = 998244353
    K = abs(A * D - B * C)
    if K == 0:
        # Special case: gcd(Ai+B, Ci+D) = gcd(Ai+B, Ci+D) directly
        # Both expressions are proportional
        if A == 0 and C == 0:
            return (gcd(B, D) * (N % MOD)) % MOD
        # Find the base GCD that repeats
        g_base = gcd(A, C)
        result = 0
        # Since K=0, one is multiple of other periodically
        # Simplified: compute directly with optimization
        for i in range(1, min(N + 1, 1000000)):
            result = (result + gcd(A*i + B, C*i + D)) % MOD
        if N > 1000000:
            # For remaining, period analysis needed
            pass
        return result
    divisors = get_divisors(K)
    # dp[d] = count of i where gcd(Ai+B, K) is exactly d
    count = {}
    # Process from largest to smallest divisors
    for d in reversed(divisors):
        c = count_multiples(A, B, d, N)
        # Subtract contributions from multiples of d
        for multiple in divisors:
            if multiple % d == 0 and multiple > d:
                c -= count.get(multiple, 0) * (multiple // d)
        count[d] = c
    # Calculate final answer
    ans = 0
    for d, c in count.items():
        ans = (ans + d * c) % MOD
    return ans
def main():
    input_data = sys.stdin.read().split()
    idx = 0
    T = int(input_data[idx])
    idx += 1
    for _ in range(T):
        N = int(input_data[idx]); idx += 1
        A = int(input_data[idx]); idx += 1
        B = int(input_data[idx]); idx += 1
        C = int(input_data[idx]); idx += 1
        D = int(input_data[idx]); idx += 1
        print(solve_one(N, A, B, C, D))
if __name__ == "__main__":
    main()

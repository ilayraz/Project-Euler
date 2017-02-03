def main(n):
    # Triangular number squared - Square pyramidal number
    return ((n * (n + 1) // 2) ** 2) - (n * (n + 1) * (2*n + 1) // 6)

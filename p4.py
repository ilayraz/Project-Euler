def getLargestPalindromeRange(min, max):
    answer = 0

    for a in range(max-1, min-1, -1):
        for b in range(a, min-1, -1):
            if a*b <= answer:
                break
            if str(a*b) == str(a*b)[::-1]:
                answer = a * b
    return answer

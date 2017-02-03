# Problem 1


def mine(max):
    return sum((set(range(0, max, 3)) | set(range(0, max, 5))) - {0})


def correct(max):
    def sumDiv(n):
        p = max // n
        return n*(p*(p+1)) // 2

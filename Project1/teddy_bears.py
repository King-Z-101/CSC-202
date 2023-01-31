def bears(n):
    num_string = str(n)
    multiplier = int(num_string[-1]) * int(num_string[-2])
    if n == 42:
        return True
    else:
        if n < 42:
            return False
        elif n % 5 == 0 and (n - 42) > 42:
            return bears(n - 42)
        elif n % 2 == 0 and (n//2) > 42:
            return bears(n//2)
        elif (n % 3 or n % 4 == 0) and n > 42:
            return bears(n - multiplier)
        else:
            return False

print(bears(41))


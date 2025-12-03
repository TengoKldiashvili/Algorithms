def count_multiples(a, b, c):
    if c < 0:
        c = -c

    if a < b:
        low = a
        high = b
    else:
        low = b
        high = a

    high_div = high // c
    low_div = (low-1) // c

    count = high_div - low_div

    return round(count)

print(count_multiples(1,10,-15))

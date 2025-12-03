def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a = 5
b = 8
c = 3
largest = find_largest(a, b, c)
print(f"The largest number is: {largest}")

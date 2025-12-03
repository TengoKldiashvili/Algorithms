x = input("Enter f(x): ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))

fa = eval(x.replace("x", str(a)))
fb = eval(x.replace("x", str(b)))

if fa * fb >= 0:
    print("Cannot find root in the interval")
else:
    c = (a + b) / 2
    fc = eval(x.replace("x", str(c)))
    if fc == 0:
        print("Root:", c)
    elif fa * fc < 0:
        print("Root in the interval [a;c]:", [a, c])
    else:
        print("Root in the interval [c;b]:", [c, b])

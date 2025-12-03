def decimal_to_binary(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result if result else "0"

def decimal_to_base4(n):
    result = ""
    while n > 0:
        result = str(n % 4) + result
        n //= 4
    return result if result else "0"

def decimal_to_hex(n):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        result = hex_digits[n % 16] + result
        n //= 16
    return result if result else "0"

def binary_to_decimal(n):
    n = str(n)
    result = 0
    power = 1
    for digit in reversed(n):
        result += int(digit) * power
        power *= 2
    return result

def base4_to_decimal(n):
    n = str(n)
    result = 0
    power = 1
    for digit in reversed(n):
        result += int(digit) * power
        power *= 4
    return result

def hex_to_decimal(n):
    n = str(n).upper()
    hex_digits = "0123456789ABCDEF"
    result = 0
    power = 1
    for digit in reversed(n):
        value = hex_digits.index(digit)
        result += value * power
        power *= 16
    return result

num_input = input("Enter number: ")
sy = int(input("Enter input number system (2,4,10,16): "))
syend = int(input("Enter target number system (2,4,10,16): "))

if sy == 10:
    decimal = int(num_input)
elif sy == 2:
    decimal = binary_to_decimal(num_input)
elif sy == 4:
    decimal = base4_to_decimal(num_input)
elif sy == 16:
    decimal = hex_to_decimal(num_input)
else:
    print("Invalid input system!")
    exit()

# --- conversion from decimal to target system ---
if syend == 10:
    result = str(decimal)
elif syend == 2:
    result = decimal_to_binary(decimal)
elif syend == 4:
    result = decimal_to_base4(decimal)
elif syend == 16:
    result = decimal_to_hex(decimal)
else:
    print("Invalid target system!")
    exit()

print(f"➡ Result: {num_input}_{sy} = {result}_{syend}")

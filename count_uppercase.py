text = input("enter text:")
count = 0
for char in text:
    if 'A' <= char <= 'Z':  
        count += 1
print("count of symbols", count)

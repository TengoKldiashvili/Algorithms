with open("test.txt", 'r', encoding='utf-8') as file:
    total_sum = 0
    count = 0
    for line in file:
        number = float(line.strip())  
        total_sum += number  
        count += 1 
        if count > 0:
                average = total_sum / count 
                print(f"avg of numbers: {average}")
        else:
                print("0 number in file.")


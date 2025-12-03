def find_second_largest(nums):
    if len(nums) < 2:
        return None  
    
    largest = second_largest = float('-inf')
    
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

nums = [12, 45, 23, 56, 89, 34, 90]
second_largest = find_second_largest(nums)
print(f"The second largest number is: {second_largest}")

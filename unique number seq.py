def unique_digits_sum(N):
    N_str = str(N)
    unique_digits = []
    
    for char in N_str:
        digit = int(char) 
        if digit not in unique_digits:
            unique_digits.append(digit)  
    total_sum = 0
    for digit in unique_digits:
        total_sum += digit
    
    return total_sum

N = int(input("Enter an integer: "))
result = unique_digits_sum(N)
print("The sum of unique digits is:", result) 
def is_strictly_increasing(N):
    previous_digit = -1
    while N > 0:
        current_digit = N % 10
        if current_digit >= previous_digit:
            return "No"
        previous_digit = current_digit
        N //= 10
    return "Yes"

N = int(input("Enter an integer: "))
result = is_strictly_increasing(N)
print(result)
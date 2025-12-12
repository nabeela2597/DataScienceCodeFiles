num = int(input("Enter a number: "))

# Convert number to string to count digits
digits = str(num)
num_digits = len(digits)

# Calculate Armstrong sum
armstrong_sum = sum(int(d)**num_digits for d in digits)

# Check condition
if armstrong_sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")

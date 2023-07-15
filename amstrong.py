num = int(input("Enter a number: "))    # get the input number from user

# find the number of digits in the input number
num_digits = len(str(num))

# initialize a variable to store the sum of cube of individual digits
sum = 0

# iterate through each digit of the input number
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

# check whether the input number is Armstrong or not
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

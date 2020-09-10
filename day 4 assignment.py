# Question 1
# Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon
# as you encounter the first armstrong number.
# Use while loop
# Output
# The first armstrong number is -----------




lb = 1042000
ub = 702648265

while (lb <= ub):
    num = lb
    order = len(str(num))

    sum = 0

    # print(startRange, digit, num, sum)
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if (lb == sum):
        print("First armstrong number: ", lb)
        break
    lb += 1

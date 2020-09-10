# # Question 2
# # Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE
# # function.
# # Output-
# # 2,3,5,7…..
lb=0
up=200
for num in range(lb, up + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

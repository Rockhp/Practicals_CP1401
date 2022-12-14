
# 1. Error Checking
#
# worker_level = int(input("Worker level: "))
# while worker_level < 1 or worker_level > 10:
#     print("Invalid worker level")
#     worker_level = int(input("Worker level: "))
#
# salary = worker_level*5000
#
# print("With worker level {}, your salary is ${:,.2f}".format(worker_level, salary))

# 2a. Number Sequences
# for num in range(1, 100 + 1):
#     if num % 2 != 0:
#         print(num, end=" ")


# 2b.
# for num in range(1896, 2021, 4):
#     print(num, end=" ")


# 2c.
# for num in range(2000, 2021,4 ):
#     print(num, end=" ")
# Explanation: All the leap years since the year was born.

# 3. Menus

# print("(S)miley (F)rowny (Q)uit")
#
# choice = input("Enter your choice: ")
#
# while choice.upper() != "q".upper():
#     if choice.upper() == "s".upper():
#         print(":)")
#     elif choice.upper() == "f".upper():
#         print(":(")
#     else:
#         print("Invalid choice")
#     choice = input("Enter your choice: ")
# print("Thank you, you have now exited the menu.")

# 4. Accumulation
# Average Age
# print("Input your age to calculate their sum and average. Input 0 to exit.")
# count = 0
# sum = 0.0
# age = 1
# while age != 0:
#     age = int(input("Enter age: "))
#     sum = sum + age
#     count += 1
# if count == 0:
#     print("Input some numbers")
# else:
#     print("Average and Sum of the above numbers are: ", sum / (count - 1), sum)

# Smileys Count
# print("(S)miley (F)rowny (Q)uit")
# choice = input("Enter your choice: ")
# smiley_count = 0
# frowny_count = 0
# while choice.upper() != "q".upper():
#     if choice.upper() == "s".upper():
#         print(":)")
#         smiley_count += 1
#     elif choice.upper() == "f".upper():
#          print(":(")
#          frowny_count += 1
#     else:
#         print("Invalid choice")
#     choice = input("Enter your choice: ")
# print("Thank you, you have now quit the menu You have printed", smiley_count, "smiley's and ", frowny_count, "frowny's")

# Total Numbers
# amount_to_add = int(input("How many numbers do you want to add up? "))
# sum = 0
# for count in range(amount_to_add):
#     sum += int(input(f"Enter number {count+1}: "))
# print("The total of those", amount_to_add, "numbers is", sum)

# 5. Guessing Game
# SECRET = 9
# guess = int(input("Guess a number: "))
# count = 1
# while guess != SECRET:
#     if guess < 9:
#         print("Too low")
#     elif guess > 9:
#         print("Too high")
#     guess = int(input("Guess a number: "))
#     count += 1
# print("You've guessed it in" + str(count) + "tries")

# 6. Nested loops
# rows = int(input("Rows: "))
# cols = int(input("Columns: "))
# nums = []
# for num in range (0,cols):
#     nums.append(num)
# for i in range(0,rows):
#     print(*nums)






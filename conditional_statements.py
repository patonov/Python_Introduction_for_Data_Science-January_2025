# number = int(input())

# is_positive = number >= 0

# if is_positive == True :
#     if number == 0:
#         print("The number is zero")
#     else:        
#         print(f"{number} is positive. Yuhuuuu!")
# else :
#     print(f"{number} is negative. Let it snow, let it snow!")

# free_friend = input()

# if free_friend == "Pesho":
#     print("We will drink too much.")
# elif free_friend == "Gosho":
#     print("We will go driving bicycles.")
# else:
#     print("Watching movie is a better option.")

# first_num = 4.50
# second_num = 5.50
# print(f"{round(first_num):.3f} {round(second_num):.2f}")

# number = int(input())
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

ticket_type = input()
if ticket_type == "regular":
    print("$1.60")
elif ticket_type == "student":
    print("1.00")
else:
    print("Invalid ticket type!")

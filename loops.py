# for i in range(0, 10):
#     print(i)


# for i in range(0, 10, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)
#     if i == 4:
#         break

# for i in range(10, 0, -1):
#     if i == 4:
#         continue
#     print(i)
# else:
#     print("The loop stopped here.")

# for i in range(0, 10):
#     for j in range(0, 10):
#         print(f"{i}{j}")

# n = int(input())
# sum = int(0)
# result_string = ""
# for i in range(1, n + 1):
#     sum += i
#     if i == n:
#         result_string += f"{i}" 
#     else:   
#         result_string += f"{i}+"
# else:
#     print(f"{result_string}={sum}")

x = int(0)
# while x < 10:
#     print(x)
#     x += 1
# else:
#     print("Oopa")

# while True:
#     print(f"You can more {x}.")
#     if x == 20:
#         break
#     x += 1

# start = int(input())
# while start > 0:
#     print(start)
#     start -= 1

# count = int(input())

# max_number = float("-inf")

# for _ in range(count) :
#     num = int(input())
    
#     if num > max_number:
#         max_number = num

# print(f"The max number is {max_number}.")

number = int(input())

temp = number
is_special = True

while temp > 0:
    digit = temp % 10

    if digit == 0 or number % digit != 0:
        is_special = False
        break

    temp //= 10

if is_special == True:
    print("Number is special.")
else:
    print("Try again later.")







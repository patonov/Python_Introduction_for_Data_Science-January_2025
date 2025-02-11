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

n = int(input())
sum = int(0)
result_string = ""
for i in range(1, n + 1):
    sum += i
    if i == n:
        result_string += f"{i}" 
    else:   
        result_string += f"{i}+"
else:
    print(f"{result_string}={sum}")


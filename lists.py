# my_list = list()

# my_string = input()

# my_list = my_string.split(" ")

# print(my_list[0])
# print(len(my_list))

# print("-".join(my_list))

# new_list = []
# last_list = [1, 2, 3, 4]

# for element in last_list:
#     new_list.append(str(element))

# print(new_list)

# print([str(element) for element in last_list])

# my_string = "abcdefghijklmnopqrstuwxyz"
# my_list = list(my_string)
# print(my_list)

# vegetables = ["carrot", "cucumber", "pumpkin"]
# vegetables.append("tomato")
# vegetables.append("tomato")
# vegetables.append("tomato")
# vegetables.append("tomato")

# vegetables.remove("tomato")
# del vegetables[len(vegetables) - 1]

# # print(vegetables[-1])
# # print(vegetables.count("tomato"))

# # for index, value in enumerate(vegetables):
# #     print(f"{index} => {value}")

# # for index in range(len(vegetables) - 1, -1, -1):    
# #     print(f"Going to delete {vegetables[index]}")
# #     vegetables.remove(vegetables[index])
# #     print(vegetables)

# while "tomato" in vegetables:
#     vegetables.remove("tomato")

# vegetables.sort(reverse=True)
# print(vegetables)
# print(vegetables.pop())

# vegetables.insert(1, "potato")
# vegetables[::-1] #vegetables.reverse()
# print(vegetables)

# tail = input()
# body = input()
# head = input()

# zoo_list = [head, body, tail]

# print(zoo_list)

# num_of_courses = int(input())
# courses = []

# for i in range(0, num_of_courses):
#     courses.append(input())

# print(courses)

# count = int(input())
# positive_numbers = []
# negative_numbers = []

# for i in range(0, count):
#     number = int(input())
#     if number >= 0:
#         positive_numbers.append(number)
#     else:
#         negative_numbers.append(number)

# print(f"The count of the positive numbers is {len(positive_numbers)}")
# print(f"The sum of the negative numbers is {sum(negative_numbers)}")


count = int(input())
searched_word = input()
all_strings = []
filltered_strings = []

for i in range(0, count):
    word = input()
    all_strings.append(word)
    if searched_word in word:
        filltered_strings.append(word)

print(filltered_strings)


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


# count = int(input())
# searched_word = input()
# all_strings = []
# filltered_strings = []

# for i in range(0, count):
#     word = input()
#     all_strings.append(word)
#     if searched_word in word:
#         filltered_strings.append(word)

# print(filltered_strings)

# count = int(input())

# filltered_nums = []
# all_nums = []

# for i in range(0, count):
#     num = int(input())
#     all_nums.append(num)

# command = input()
# if command == "even":
#     filltered_nums = [num for num in all_nums if num % 2 == 0 ]
# if command == "odd":
#     filltered_nums = [num for num in all_nums if num % 2 != 0 ]
# if command == "positive":
#     filltered_nums = [num for num in all_nums if num >= 0 ]
# if command == "positive":
#     filltered_nums = [num for num in all_nums if num < 0 ]

# print(filltered_nums)


# class Person:
#     age = 18
#     residence = "Pleven"
#     number_of_instances = 0

#     def __init__(self, name: str, salary: int):
#         self.name = name
#         self.salary = salary
#         Person.number_of_instances += 1


# person = Person("Nikolay", 1011)

# print(person.name)
# print(person.salary)
# print(Person.number_of_instances)

# print(person.residence)
# print(person.age)

# pesho_persona = Person("Pesho", 2021)
# print(Person.number_of_instances)

# misho_persona = Person("Misho", 2221)
# misho_persona.favorite_song = "Ochi, ochi" #very bad practice!
# print(Person.number_of_instances)
# print(misho_persona.favorite_song)

# list_of_numbers = input().split()
# opposite_numbers = []

# for num in list_of_numbers:
#     opposite_number = -int(num)
#     opposite_numbers.append(opposite_number)

# print(opposite_numbers)

# def invert_values(nums: list[str]) -> list[int]:
#     opposite_numbers = []

#     for num in nums:
#         opposite_number = -int(num)
#         opposite_numbers.append(opposite_number)
    
#     return opposite_numbers

# list_of_numbers = input().split()
# print(invert_values(list_of_numbers))

# input_list = input().split()

# doubled_list = list(map(lambda x: int(x) * 2, input_list))
# casted_list = list(map(lambda x: int(x), input_list))

# print(doubled_list)

# filtered_list = [num for num in casted_list if num % 2 == 0]
# print(filtered_list)

# nums = [1, 2, 3]
# nums[0], nums[1], nums[2] = nums[2], nums[1], nums[0]
# print(nums)

# mixed_nums = [1, 1, 3, 2, 1, 5, 6]
# unique_nums = set(mixed_nums)
# print(unique_nums)

# from functools import reduce

# nums_to_reduce = [1, 1, 3, 2, 1, 5, 6]
# sum = reduce(lambda x, y: x + y, nums_to_reduce)
# print(sum)
# print("proud of being Js disciple...")

# print(f"The max value here is: {reduce(lambda a, b: a if a > b else b, nums_to_reduce)}")

# words = input().split()
# pallindromes = [word for word in words if word == word[::-1]]
# print(pallindromes)

names_unsorted = input().split()
names = list(sorted(names_unsorted, key= lambda name: (-len(name), name)))
print(names)
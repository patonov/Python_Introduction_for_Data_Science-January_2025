# import math

# speed = float(input())
# fuel_cost = float(input())

# distance = 384400 * 2
# travel_time = distance / speed
# total_time = math.ceil(travel_time) + 3

# fuel = (fuel_cost * distance) / 100

# print(total_time)
# print(round(fuel))


# n = int(input())

# two_devided = 0
# three_devided = 0
# four_devided = 0

# for i in range(0, n):
#     a = int(input())
#     if a % 2 == 0:
#         two_devided += 1
#     if a % 3 == 0:
#         three_devided += 1
#     if a % 4 == 0:
#         four_devided += 1


# two_div_perc = two_devided / n 
# three_div_perc = three_devided / n
# four_div_perc = four_devided / n 

# print(f"{(two_div_perc * 100):.2f}%")
# print(f"{(three_div_perc * 100):.2f}%")
# print(f"{(four_div_perc * 100):.2f}%")

# array = input().split()
# n = int(input())

# target = [num for num in array if int(num) < n]

# print(f"{' '.join(target)}")

command = input()
heroes = {}

while command != "End":
    
    if command.split()[0] == "Enroll":
        if command.split()[1] in heroes.keys():
            print(f"{command.split()[1]} is already enrolled.")
        else:
            hero = command.split()[1]
            heroes[hero] = []
    if command.split()[0] == "Learn":
        name = command.split()[1]
        spell = command.split()[2]
        if name not in heroes.keys():
            print(f"{name} doesn't exist.")
        else:
            if spell in heroes[name]:
                print(f"{name} has already learnt {spell}.")
            else:
                heroes[name].append(spell)
    if command.split()[0] == "Unlearn":
        name = command.split()[1]
        spell = command.split()[2]
        if name not in heroes.keys():
            print(f"{name} doesn't exist.")
        else:
            if spell not in heroes[name]:
                print(f"{name} doesn't know {spell}.")
            else:
                heroes[name].remove(spell)

    command = input()

print("Heroes:")
for hero in heroes.keys():
    print(f"== {hero}: {', '.join(heroes[hero])}")

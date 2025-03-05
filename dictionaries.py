age_dictionary = {"ivan": 16, "pencho": 19, "mitko": 21, "dimitrichko": 18}

# print(age_dictionary.keys())

# for key, value in age_dictionary.items():
#     print(f"{key} and {value}")

# for name in age_dictionary.keys():
#     age_dictionary[name] += 1

# age_dictionary["uyu"] = 11

# print(age_dictionary)

# name = input().lower()

# if name in age_dictionary.keys():
#     print(age_dictionary[name])

# children = {"first_child": "Ivancho", "toys": ["monkey", "dragon", "ball"]}
# toys = {"plastic": {"animals": ["monkey", "dragon", "rabit"]}, "rubber": {"balls": ["football", "tenis ball"]}}

# print(toys["plastic"]["animals"][1])

# copy_toys = toys.copy()
# print(f"The copy of the toys dictionary is: {copy_toys}")

# copy_toys.clear()
# print(copy_toys)

# print(toys.pop("plastic"))
# print(toys.popitem())

# del children["toys"]  
# print(children)

children_names = ["gogi", "dimitrichko", "mimi"]
children_ages = [18, 11, 17]

#children_data = dict(zip(children_names, children_ages))
children_data = {name: age for (name, age) in zip(children_names, children_ages)}
print(children_data)
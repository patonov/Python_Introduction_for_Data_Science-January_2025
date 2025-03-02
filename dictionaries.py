age_dictionary = {"ivan": 16, "pencho": 19, "mitko": 21, "dimitrichko": 18}

# print(age_dictionary.keys())

# for key, value in age_dictionary.items():
#     print(f"{key} and {value}")

# for name in age_dictionary.keys():
#     age_dictionary[name] += 1

# age_dictionary["uyu"] = 11

# print(age_dictionary)

name = input().lower()

if name in age_dictionary.keys():
    print(age_dictionary[name])
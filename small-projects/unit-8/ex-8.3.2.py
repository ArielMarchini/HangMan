mariah = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

num = int(input("Enter a number between 1 and 7: "))

if num == 1:
    print(mariah["last_name"])

elif num == 2:
    birth_date = mariah["birth_date"]
    month = birth_date.split(".")[1]
    print(month)

elif num == 3:
    num_hobbies = len(mariah["hobbies"])
    print(num_hobbies)

elif num == 4:
    last_hobby = mariah["hobbies"][-1]
    print(last_hobby)

elif num == 5:
    mariah["hobbies"].append("Cooking")
    print(mariah["hobbies"])

elif num == 6:
    birth_date = mariah["birth_date"]
    day, month, year = birth_date.split(".")
    birth_date_tuple = (int(day), int(month), int(year))
    print(birth_date_tuple)

elif num == 7:
    birth_year = int(mariah["birth_date"].split(".")[-1])
    age = 2023 - birth_year
    mariah["age"] = age
    print(mariah["age"])

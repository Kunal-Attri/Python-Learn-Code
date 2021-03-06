# 'zip' method to iterate over multiple lists

names = ["Kunal", "Rahul", "Preeti"]
gender = ['male', 'male', 'female']
ages = [17, 18, 19]

for name, g, age in zip(names, gender, ages):
    print(f"{name} is a {g} and is {age} years old.")


# Thank you !!!

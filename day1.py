from datetime import date

name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))

current_year = date.today().year
year_turns_60 = current_year + (60 - age)

print(f"Hello, {name}! You are {age} years old.")

if age < 60:
    print(f"You will turn 60 in the year {year_turns_60}.")
elif age == 60:
    print("You are turning 60 this year!")
else:
    print(f"You turned 60 in the year {year_turns_60}.")
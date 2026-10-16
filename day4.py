


marks = [45, 78, 32, 90, 35, 60, 28, 85]
names = ["ravi", "anu", "kumar", "priya", "john", "meena", "sam", "divya"]

highest = max(marks)
lowest = min(marks)

average = sum(marks) / len(marks)

passes = 0
for m in marks:
    if m >= 35:
        passes = passes + 1


upper_names = [n.upper() for n in names]

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Passes:", passes)
print("Names:", upper_names)

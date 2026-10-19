def average(marks):
    return sum(marks) / len(marks)


def highest(marks):
    return max(marks)


def lowest(marks):  
    return min(marks)


def grade(score, pass_mark=40):
    
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= pass_mark:
        return "D"
    else:
        return "F"

marks = [85, 92, 67, 45, 78, 33, 90]

avg = average(marks)

print(f"Marks   : {marks}")
print(f"Average : {avg:.2f}")
print(f"Highest : {highest(marks)}")
print(f"Lowest  : {lowest(marks)}")
print(f"Grade of average ({avg:.2f}): {grade(avg)}")


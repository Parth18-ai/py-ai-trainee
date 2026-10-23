

FILE_NAME = "students.csv"


students = {}


def add_student():
    name = input("Student name: ")

    # Check the name first
    if name == "" or "," in name:
        print("Name cannot be empty or contain a comma")
        return                                  

    try:
        marks = float(input("Marks (0-100): "))  
        if marks < 0 or marks > 100:
            raise ValueError                     
    except ValueError:
        print("Marks must be a number from 0 to 100")
    else:
      
        students[name] = marks
        print("Student added!")


def list_students():
    if len(students) == 0:
        print("No students yet")
    else:
        for name, marks in students.items():
            print(name, "-", marks)


def save_students():
    try:
        with open(FILE_NAME, "w") as file:       
            file.write("name,marks\n")           
            for name, marks in students.items():
                file.write(f"{name},{marks}\n")  
    except OSError:
        print("Could not save the file")
    else:
        print("Saved to", FILE_NAME)
    finally:
        print("(save finished)")                 

def load_students():
    try:
        with open(FILE_NAME) as file:            
            lines = file.readlines()
            loaded = {}
            for line in lines[1:]:               
                name, marks = line.strip().split(",")
                loaded[name] = float(marks)
    except FileNotFoundError:
        print("File not found. Save some students first")
    except ValueError:
        print("The file is damaged")
    else:
        students.clear()
        students.update(loaded)
        print("Loaded from", FILE_NAME)



while True:
    print("\n1. Add  2. List  3. Save  4. Load  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        list_students()
    elif choice == "3":
        save_students()
    elif choice == "4":
        load_students()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Please choose 1 to 5")
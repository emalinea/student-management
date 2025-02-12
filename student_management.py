import json

students = []

def add(students, id, name, age, grade, subjects):
    student = {"id": id, "name": name, "age": age, "grade": grade, "subjects": subjects}
    students.append(student)
    return students

def id_unique(students, id):
    for student in students:
        if student["id"] == id:
            return False
    return True

def addStudent():
    while True:
        try:
            while True:
                id = input("Enter id:\n")
                if not id.isnumeric():
                    print("ID must be a number. Please try again.")
                elif not id_unique(students, id):
                    print(f"ID {id} already exists. Please enter a new one.")
                else:
                    break
            while True:
                name = input("Enter name:\n")
                if name.isnumeric():
                    print("Name can not contain numbers. Please try again.")
                else:
                    break
            while True:
                age = input("Enter age:\n")
                if not age.isnumeric():
                    print("Age must be number. Please try again.")
                else:
                    break
            while True:
                grade = input("Enter grade:\n")
                if grade.isnumeric():
                    print("Grade can not be a number. Please try again.")
                else:
                    break
            while True:
                subjects = input("Enter subjects:\n")
                if subjects.isnumeric():
                    print("Subjects can not be numbers. Please try again.")
                else:
                    break
            add(students, id, name, age, grade, subjects)
            print("Student added successfully. Please insert your choice.")
            break
        except Exception as e:
            print(f"Error adding student: {e}")
            break

def display(students, id):
    for student in students:
        if student["id"] == int(id):
            return student
    return None

def displayStudent():
    id = input("Enter the ID to view student:\n")
    student = display(students, id)
    if student:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Subjects: {student['subjects']}")
    else:
        print("Student not found")

def update_student(students, id, updates):
    for student in students:
        if student["id"] == int(id):
            for key, value in updates.items():
                if key in student:
                    student[key] = value
            return student
    return None

def updateStudent():
    id = input("Enter id to update:\n")
    student = display(students, id)
    if student:
        print(f"Updating student: {student['name']}")
        new_name = input(f"Enter new name to update (leave blank to keep) '{student['name']}'):\n") or student["name"]
        new_age = input(f"Enter new age to update (leave blank to keep '{student['age']}'):\n") or student["age"]
        new_grade = input(f"Enter new grade to update (leave blank to keep '{student['grade']}':\n") or student["grade"]
        new_subjects = input(f"Enter new subjects to update (leave blank to keep '{student['subjects']}'):\n") or student["subjects"]
        updates = {
            "name": new_name,
            "age": new_age,
            "grade": new_grade,
            "subjects": new_subjects,
        }             
        update_student(students, id, updates)
        print("Student's information is now updated.")
    else:
        print("Student not found.") 

def delete_student(students, student_id):
    return [s for s in students if s["id"] != int(student_id)]

def deleteStudent():
    global students
    id = input("Enter the id to delete:\n")
    if display(students, id):
        students = delete_student(students, id)
        save_Students_to_file()
        print(f"Student with ID {id} was deleted.")
    else:
        print("Student not found. Please try again.")

def save_Students_to_file(filename='students.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(students, file, indent=4)
    except Exception as e:
        print(f"Error saving student: {e}")

def load_Students_from_file(filename='students.json'):
    global students
    try:
        with open(filename, 'r') as file:
            students = json.load(file)
            students = [
                {
                    "id": int(student["id"]),
                    "name": student["name"],
                    "age": int(student["age"]),
                    "grade": student["grade"],
                    "subjects": student["subjects"]
                }
                for student in students
            ]
        print("Students loaded from file.")
    except FileNotFoundError:
        print("No saved data found. Starting with an empty list.")
    except Exception as e:
        print(f"Error loading students: {e}")

def main():
    load_Students_from_file()
    while True:
        try:
            choice = int(input("""
            1. Add a new student
            2. View all students
            3. Update a student's information
            4. Delete a student's information
            5. Save and exit\n                                                                                        
        """)) 
            if (choice == 1):
                addStudent()
            elif (choice == 2):
                if len(students) == 0:
                    print("No student found. Please try again.")
                else:    
                    for student in students:
                        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Subjects: {student['subjects']}")
            elif (choice == 3):
                updateStudent()
            elif (choice == 4):
                deleteStudent()
            elif (choice == 5):
                save_Students_to_file()
                print("File has been updated.") 
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()                                                           



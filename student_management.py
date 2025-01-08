import json

# enklare jobba med CLASSES, kolla bilden
# exempel:
""" class Student:
    def __init__(self, student_id, name, age, grade, subjects):""" 



# Global variable to store students
students = []

# Function to add a new student
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student = {"id": student_id, "name": name, "age": age}
    students.append(student)
    print(f"Student {name} added successfully!")

# Function to view all students
def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    print()

# Function to update a student's information
def update_student():
    student_id = input("Enter the student ID to update: ")
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        print(f"Updating student {student['name']} (ID: {student['id']})")
        student['name'] = input("Enter new name: ")
        student['age'] = input("Enter new age: ")
        print("Student information updated.")
    else:
        print("Student not found.")

# Function to delete a student
def delete_student():
    student_id = input("Enter the student ID to delete: ")
    global students
    students = [s for s in students if s["id"] != student_id]
    print(f"Student with ID {student_id} has been deleted.")

# Function to save students to a file
def save_students():
    with open('students.json', 'w') as file:
        json.dump(students, file)
    print("Students have been saved.")

# Function to load students from a file
def load_students():
    global students
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    print("Student data loaded.")

# Function to display the menu
def show_menu():
    print("\nMenu:")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update a student's information")
    print("4. Delete a student")
    print("5. Save and exit")

# Main function
def main():
    load_students()  # Load student data when the program starts

    while True:
        show_menu()
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            save_students()  # Save the students before exiting
            print("Exiting the program.")
            break  # Exit the loop
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()

import unittest
import json
import os
import student_management


class StudentManagementTest(unittest.TestCase):
    def test_add(self):
        res = student_management.add([], 1, "Olle", 20, "VG", "Math")
        self.assertEqual(res, [{ "id": 1, "name": "Olle", "age": 20, "grade": "VG", "subjects": "Math"}] )
    

    def test_display(self):
        students = [
            { "id": 1, "name": "Olle", "age": 20, "grade": "VG", "subjects": "Math" }
        ]
        student = student_management.display(students, 1)
        self.assertEqual(student, { "id": 1, "name": "Olle", "age": 20, "grade": "VG", "subjects": "Math" })  


    def test_update_student(self):
        students = [
            { "id": 1, "name": "Olle", "age": 20, "grade": "VG", "subjects": "Math" }
        ]
        updates = {
            "name": "Olle updated",
            "age": 21,
            "grade": "G",
            "subjects": "Geography"
        }
        updated_student = student_management.update_student(students, 1, updates)
        self.assertEqual(updated_student["name"], "Olle updated")
        self.assertEqual(updated_student["age"], 21)
        self.assertEqual(updated_student["grade"], "G")
        self.assertEqual(updated_student["subjects"], "Geography")    


    def test_delete_student(self):
        student_management.students = [
            { "id": 1, "name": "Olle", "age": 20, "grade": "VG", "subjects": "Math" }
        ]
        
        student_management.students = student_management.delete_student(student_management.students, 1)
        
        remaining_ids = [s["id"] for s in student_management.students]
        self.assertNotIn(1, remaining_ids)
        self.assertEqual(len(student_management.students), 0)
        
        student_management.save_Students_to_file(self.test_filename)
        
        with open(self.test_filename, 'r') as f:
            saved_data = json.load(f)
            print("Saved data:", saved_data)

        self.assertEqual(saved_data, [])


    def setUp(self):
        self.test_filename = 'test_students.json'
        self.test_data = [{"id": 1, "name": "Olle", "age": 20, "grade": "VG", "subjects": "Math"}]
        with open(self.test_filename, 'w') as f:
            json.dump(self.test_data, f, indent=4)
        student_management.students = []


    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)


    def test_save_Students_to_file(self):
        student_management.students = []
        student_management.add(student_management.students, 1, "Olle", 20, "VG", "Math")
        student_management.save_Students_to_file(self.test_filename)
       
        with open(self.test_filename, 'r') as f:
            saved_data = json.load(f)

        self.assertEqual(saved_data, student_management.students)


    def test_load_Students_from_file(self):
        with open(self.test_filename, 'w') as f:
            json.dump(self.test_data, f, indent=4)
        student_management.students = []
        student_management.load_Students_from_file(self.test_filename)
        self.assertEqual(student_management.students, self.test_data)        


if __name__ == '__main__':
    unittest.main()

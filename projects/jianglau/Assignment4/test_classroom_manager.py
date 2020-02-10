import unittest
import classroom_manager as cm

class TestStudent(unittest.TestCase):
    def test_init(self):
        student = cm.Student(1, "Laura", "Jiang")
        self.assertEqual(student.id, 1)
        self.assertEqual(student.first_name, "Laura")
        self.assertEqual(student.last_name, "Jiang")
        self.assertEqual(student.assignments, [])

    def test_get_name(self):
        student = cm.Student(1, "Laura", "Jiang")
        name = student.get_full_name()
        self.assertEqual(name, "Laura Jiang")

    def test_submit_assignment(self):
        student = cm.Student(1, "Laura", "Jiang")
        assignment1 = cm.Assignment("Assignment-1", 10)
        assignment2 = cm.Assignment("Assignment-2", 10)
        student.submit_assignment(assignment1)
        student.submit_assignment(assignment2)
        self.assertEqual(len(student.assignments), 2)
        self.assertEqual(student.assignments[0].name, "Assignment-1")
        self.assertEqual(student.assignments[1].name, "Assignment-2")

    def test_get_assignments(self):
        student = cm.Student(1, "Laura", "Jiang")
        assignment1 = cm.Assignment("Assignment-1", 10)
        assignment2 = cm.Assignment("Assignment-2", 10)
        assignment3 = cm.Assignment("Assignment-3", 10)
        student.submit_assignment(assignment1)
        student.submit_assignment(assignment2)
        student.submit_assignment(assignment3)
        self.assertEqual(len(student.assignments), 3)
        assignments = student.get_assignments()
        self.assertEqual(len(assignments), 3)
        self.assertEqual(assignments[0].name, "Assignment-1")

    def test_get_one_assignment(self):
        student = cm.Student(1, "Laura", "Jiang")
        assignment1 = cm.Assignment("Assignment-1", 10)
        student.submit_assignment(assignment1)
        self.assertEqual(len(student.assignments), 1)
        assignment = student.get_assignment("Assignment-1")
        self.assertEqual(assignment.name, "Assignment-1")

    def test_get_average(self):
        student = cm.Student(1, "Laura", "Jiang")
        assignment1 = cm.Assignment("Assignment-1", 10)
        assignment2 = cm.Assignment("Assignment-2", 10)
        assignment3 = cm.Assignment("Assignment-3", 10)
        assignment1.grade = assignment2.grade = 10
        assignment3.grade = None
        student.submit_assignment(assignment1)
        student.submit_assignment(assignment2)
        student.submit_assignment(assignment3)
        average_grade = student.get_average()
        self.assertEqual(average_grade, 10)

    def test_remove_assignment(self):
        student = cm.Student(1, "Laura", "Jiang")
        assignment1 = cm.Assignment("Assignment-1", 10)
        assignment2 = cm.Assignment("Assignment-2", 10)
        student.submit_assignment(assignment1)
        student.submit_assignment(assignment2)
        self.assertEqual(len(student.assignments), 2)
        self.assertEqual(student.assignments[1].name, "Assignment-2")
        student.remove_assignment("Assignment-2")
        self.assertEqual(len(student.assignments), 1)
        self.assertEqual(student.assignments[0].name, "Assignment-1")

class TestAssignment(unittest.TestCase):
    def test_init(self):
        assignment = cm.Assignment("Assignment-1", 10)
        self.assertEqual(assignment.name, "Assignment-1")
        self.assertEqual(assignment.max_score, 10)
        self.assertEqual(assignment.grade, None)

    def test_assign_grade(self):
        assignment = cm.Assignment("Assignment-1", 10)
        assignment.assign_grade(10)
        self.assertEqual(assignment.grade, 10)
        assignment.assign_grade(11)
        self.assertEqual(assignment.grade, None)


if __name__ == '__main__':
    unittest.main()

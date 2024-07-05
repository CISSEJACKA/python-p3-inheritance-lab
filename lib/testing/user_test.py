# lib/testing/user_test.py
import pytest
from lib.user import User
from lib.teacher import Teacher
from lib.student import Student

def test_user():
    user = User("John", "Doe")
    assert user.first_name == "John"
    assert user.last_name == "Doe"

def test_teacher():
    teacher = Teacher("Jane", "Smith")
    assert teacher.first_name == "Jane"
    assert teacher.last_name == "Smith"
    assert len(teacher.knowledge) > 0
    assert teacher.teach() in teacher.knowledge

def test_student():
    student = Student("Alice", "Johnson")
    assert student.first_name == "Alice"
    assert student.last_name == "Johnson"
    assert student.knowledge == []
    student.learn("new knowledge")
    assert "new knowledge" in student.knowledge

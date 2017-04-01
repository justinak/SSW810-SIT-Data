# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:47:05 2017


Create a data repository for Stevens Institute of Technology containing information about students, instrustors and grades.

For Student:
    -track required courses
    -track courses completed
    -track grades
    -calculate GPA
    
    METHODS: study, register
    
For Intructor:
    
    METHODS: teach
    
For Faculty Advisor:
    -create student study plans

Homework 9:
    -Build framework to summarize student and instructor data
    -Read data from each of 3 files
    -Store in data structure that is easy to process
    
    PHASE 1:
        CLASS REPOSITORY
        -Initialize repository
        -Read Students data file
        -Store students (Student Collaborator)
        -Read Instructor data file
        -Store instructors (Instructor Collaborator)
        -Read Grades data file
        -Assign course/grade to student (Student Collaborator)
        -Assign course to instructor (Instructor Collaborator)
        -Create Student Summary (Student, PrettyTable)
        -Create Instructor Summary (Instructor, PrettyTable)
        
        CLASS STUDENT
        -Initialize Student
        -Store student CWID (Repository Collaborator)
        -Store student name (Repository Collaborator)
        -Store student major (Repository Collaborator)
        -Note courses taken (Grade Collaborator)
        -Provide set of courses taken
        
        CLASS INSTRUCTOR 
        -Initialize instructor
        -Store instructor CWID
        -Store instructor name
        -Store instructor department
        -Store courses taught (Grade Collaborator)
        -Store # students in each course (Grade Collaborator)
        -Return courses taught
        -Return number students in each course
        
        CLASS GRADE
        -Initialize Grade
        -Store student CWID
        -Store course
        -Store grade
        -Store instructor CWID
"""

import unittest
from prettytable import PrettyTable
from collections import defaultdict


class Repository:
    """Create a repository to hold data structures """
    def __init__(self): # initialize repository
        self.students = dict() # key: student CWID, value: instance of class Student
        self.instructors = dict() # key: instructor CWID, value: instance of class Instructor
        self.grades = list()

    def read_students(self, students_file):
        try:
            fp = open(students_file, 'r')
        except FileNotFoundError:
            print("File", students_file, "cannot be read, not a .txt file" )
        else:
            for line in fp:
                CWID, name, major = line.strip.split("\t")
                self.students[CWID]=Student(CWID, name, major)
            
    def read_instructors(self, instructors_file):
        try:
            fp = open(instructors_file, 'r')
        except FileNotFoundError:
            print("File", instructors_file, "cannot be read, not a .txt file" )
        else:
            for line in fp: 
                CWID, name, dept = line.strip.split("\t")
                self.instructors[CWID]=Instructor(CWID, name, dept) 

    def read_grades(self, grades_file): 
        try:
            fp = open(grades_file, 'r')
        except FileNotFoundError:
            print("File", grades_file, "cannot be read, not a .txt file" )
        else:
            for line in fp:
                student_CWID, course, grade, instructor_CWID = line.strip.split("\t")
                self.grades.append(Grade(student_CWID, course, grade, instructor_CWID))
                
    def assign_course(self):
        student = ""
        instructor = ""
        if student:
            for grade in Student.courses_taken: # loop through all grades using Student collaborator
                st_new_course = grade.Student.st_add_course
                print("Student, add new course", st_new_course)
        elif instructor:
            for grade in Instructor.courses_taught: 
                in_new_course = grade.Intructor.in_new_course # assign course using Instructor collaborator
                print("Instructor", in_new_course)
    
    def student_summary(self):
        """ Create a table summarizing all the info about students from students.txt and grades.txt """
        student_table = PrettyTable(['CWID', 'Name', 'Completed Courses'])
        student_table.add_row([Student.CWID, Student.name, Student.coures_taken])
        print(student_table)
        
    def instructor_summary(self):
        """ Create a table summarizing all the info about instructors from instructors.txt and grades.txt """
        instructor_table = PrettyTable(['CWID', 'Name', 'Dept', 'Course', 'Students'])
        instructor_table = PrettyTable([Instructor.CWID, Instructor.name, Instructor.dept, Grade.course, Instructor.courses_taught])
        print(instructor_table)
        
        
class Student:
    def __init__(self, CWID, name, major): # initialize student class
        self.CWID = CWID
        self.name = name
        self.major = major
        self.courses_taken = defaultdict(str) #key: course, value: grade
        
    def st_add_course(self, grade): # counting how many grades there are for a given course which determines number of student who have taken the course
        self.courses_taken[grade.course]=grade.grade 
        return sorted(self.courses_taken)
        
    def courses_completed(self, course):
        """Create a defaultdict(str) where key==CWID, value=={dict w/ key==course, value==grade} showing which 
           courses a student has completed"""
        grades = 0 # instanciating that there are 0 grades for the first course
        for grade in Student.st_add_course(): # for every student that has a grade for a course
            grades +=1 # count how many grades the course has
            add_course = self.courses_taken.append[course][grades] # add the course and how many grades were counted for it      
            return add_course  
            # print(Grade.courses_completed[CWID_st][grade.add_course])
           
    
class Instructor:
    def __init__(self, CWID, name, dept): # initialize instructor class
        self.CWID = CWID
        self.name = name
        self.dept = dept
        self.courses_taught = defaultdict(int)
        
    def in_add_course(self, course, grade):
        self.courses_taught[grade.course]=grade.course
        return self.courses_taught
        
    def courses_taught(self, course):
        """Create a defaultdict(int) where key==course, value==num_students"""
        taught_course = self.courses_taught.append[course]
        return taught_course
    
        
class Grade:
    def __init__(self, CWID_st, course, grade, CWID_in): # initialize grade class
        self.CWID_st = CWID_st
        self.course = course
        self.grade = grade
        self.CWID_in = CWID_in 
    

def main():  
    try:  
        students = Repository.read_students("C:\Python27\students.txt")
    except FileNotFoundError:
        print("Invalid directory")
    try:
        instructors = Repository.read_instructors("C:\Python27\instructors.txt")
    except FileNotFoundError:
        print("Invalid directory")
    try:
        grades = Repository.read_grades("C:\Python27\grades.txt")
    except FileNotFoundError:
        print("Invalid directory")
        
    while True:
        students.st_add_course('A', 'B', 'C', 'D')
        students.courses_completed()
        instructors.in_add_course('SSW 567', 'SSW 564', 'SSW 687', 'SSW 555', 'SSW 689', 'SSW 800', 'SSW 750', 'SSW 611', 'SSW 645')
        instructors.courses_taught()
        grades()
        break
        
  
class StudentPrettyTableTest(unittest.TestCase):
    """Test Pretty Table"""
    def test_summary(self):
        """ Test Student summary table """
        CWID, name, courses_taken = Repository.student_summary
        self.assertEqual(CWID, 10103)
        self.assertEqual(name, 'Baldwin, C')
        self.assertEqual(courses_taken, ['SSW 567', 'SSW 564', 'SSW 687'])  

        
class InstructorPrettyTableTest(unittest.TestCase):
    """ Test Pretty Table """
    def test_summary(self):
        """ Test Instructor summary table """
        CWID, name, dept, course, students = Repository.instructor_summary
        self.assertEqual(CWID, 98764)
        self.assertEqual(name, 'Feynman, R')
        self.assrtEqual(dept, 'SFEN')
        self.assertEqual(course, 'SSW 687')
        self.assertEqual(students, 3)
        
# class StudentsInCourseTest(unittest.TestCase):
        

    if __name__ == '__main__':
        unittest.main(exit=False, verbosity=3)
        main()
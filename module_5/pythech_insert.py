# Import MongoClient from pymongo module
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.n37za4m.mongodb.net/pytech"

# Create a MongoClient object and pass the URL to it
client = MongoClient(url)

# Connect to the pytech database
db = client.pytech

""" 
Create three student documents
"""

# Thorin Oakenshield's data document 
thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
    "enrollments": [
        {
            "term": "Semester 2",
            "gpa": "4.0",
            "start_date": "January 10, 2022",
            "end_date": "April 14, 2022",
            "courses": [
                {
                    "course_id": "CYB310",
                    "description": "Database Security",
                    "instructor": "Professor Le",
                    "grade": "A-"
                },
                {
                    "course_id": "CYB330",
                    "description": "Intro to Programming",
                    "instructor": "Professor Le",
                    "grade": "B+"
                }
            ]
        }
    ]
}

# Bilbo Baggins data document 
bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Semester 2",
            "gpa": "3.52",
            "start_date": "January 10, 2023",
            "end_date": "April 14, 2023",
            "courses": [
                {
                    "course_id": "CYB310",
                    "description": "Database Security",
                    "instructor": "Professor Le",
                    "grade": "B+"
                },
                {
                    "course_id": "CYB330",
                    "description": "Intro to Programming",
                    "instructor": "Professor Le",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# Frodo Baggins data document
frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Semester 2",
            "gpa": "1.5",
            "start_date": "January 10, 2023",
            "end_date": "April 14, 2023",
            "courses": [
                {
                    "course_id": "CYB310",
                    "description": "Database Security",
                    "instructor": "Professor Le",
                    "grade": "C"
                },
                {
                    "course_id": "CYB330",
                    "description": "Intro Programming",
                    "instructor": "Professor Le",
                    "grade": "B"
                }
            ]
        }
    ]
}

# Get the students collection 
students = db.students

# Insert statements with output 
print("\n  -- INSERT STATEMENTS --")

# Insert Thorin Oakenshield's document into the students collection
thorin_student_id = students.insert_one(thorin).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))

# Insert Bilbo Baggins' document into the students collection
bilbo_student_id = students.insert_one(bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

# Insert Frodo Baggins' document into the students collection
frodo_student_id = students.insert_one(frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")
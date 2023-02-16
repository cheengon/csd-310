# Import the necessary module for connecting to MongoDB
from pymongo import MongoClient

# Set the MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.n37za4m.mongodb.net/pytech"

# Connect to the MongoDB cluster using the connection string
client = MongoClient(url)

# Connect to the "pytech" database within the cluster
db = client.pytech

# Get the "students" collection from the "pytech" database
students = db.students

# Find all students in the "students" collection
student_list = students.find({})

# Display a message before the list of students
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over each document in the student_list and display the student information
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Define a student to be added to the "students" collection
student_doc = {
    "student_id": "1010",
    "first_name": "Mario",
    "last_name": "Calderon"
}

# Insert the student into the "students" collection and save the document ID
student_doc_id = students.insert_one(student_doc).inserted_id

# Display a message after inserting the new student
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(student_doc_id))

# Find the new student by the student ID (1010) using the find_one() method
student_test_doc = students.find_one({"student_id": "1010"})

# Display the test document information
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# Remove the student by student ID (1010) using the delete_one() method
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# Find all students in the "students" collection again
new_student_list = students.find({})

# Display a message before the list of remaining students
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over each document in the new_student_list and display the student information
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Display a message to signal the end of the program and wait for user input before closing the program
input("\n\n  End of program, press any key to continue...")

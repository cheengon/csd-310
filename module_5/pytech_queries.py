# Import MongoClient class from pymongo library
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.n37za4m.mongodb.net/pytech"

# Create a new MongoClient instance and connect to the MongoDB cluster using the connection string
client = MongoClient(url)

# Access the pytech database from the connected MongoDB cluster
db = client.pytech

# Access the students collection from the pytech database
students = db.students

# Find all students in the students collection and return the results as a cursor
student_list = students.find({})

# Display message
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over the cursor and output the results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Find a document in the students collection with the "student_id" field equal to "1008" and return the result as a dictionary
bilbo = students.find_one({"student_id": "1008"})

# Display message
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

# Output the results
print("  Student ID: " + bilbo["student_id"] + "\n  First Name: " + bilbo["first_name"] + "\n  Last Name: " + bilbo["last_name"] + "\n")

# Display exit message and wait for user to press a key before continuing
input("\n\n  End of program, press any key to continue...")

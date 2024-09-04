# Create the student dictionary
student = {
    'first_name': 'JOYDEEP',
    'last_name': 'KARMAKAR',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Node Js', 'DevOps'],
    'country': 'India',
    'city': 'KOLKATA',
    'address': 'TARULIA 3RD LANE'
}

# I. Get the length of the student dictionary
length_of_student_dict = len(student)
print("Length of the student dictionary:", length_of_student_dict)

# II. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

# III. Modify the skills values by adding one or two skills
student['skills'].extend(['Cloud Computing', 'Backend Development'])
print("Modified skills:", student['skills'])

# IV. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)

# V. Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values:", values_list)

# VI. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("List of tuples (items):", student_items)

# VII. Delete one of the items in the dictionary
del student['marital_status']
print("Dictionary after deleting 'marital_status':", student)

# VIII. Delete the dictionary completely
del student

# Trying to print student will raise an error because it's deleted
try:
    print(student)
except NameError:
    print("The student dictionary has been deleted.")

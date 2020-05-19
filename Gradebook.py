#Defining a mock scenario to update a gradebook
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#Creating lists
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

#Appending the lists
subjects.append('computer science')
grades.append(100)

#Combining the lists
gradebook = list(zip(subjects, grades))

#Appending gradebook
gradebook.append(('visual arts', 93))

#Testing the code
print(gradebook)

#Combining last semester gradebook with the current one
full_gradebook = gradebook + last_semester_gradebook

#Testing the code
print(full_gradebook)
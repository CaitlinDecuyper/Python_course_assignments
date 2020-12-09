from faker import Faker  # Before running this script, run `pip install faker`
from numpy.random import normal
import numpy as np

# First, let me generate some fake data for you...
fake = Faker()
students = []
for i in range(100):
    students.append({
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address(),
        'maths': np.clip(normal(3, .5), 0, 4),
        'linguistics': np.clip(normal(3, .5), 0, 4),
        'psychology': np.clip(normal(3, .5), 0, 4)
    })

# The students variable now contains a list of dictionaries, where each dictionary contains 6 key-value pairs.
# Now, let's try out some things!

first_names = []
last_names = []
addresses = []
maths_grades = []
linguistics_grades = []
psychology_grades = []

# Can you write a loop that fills the above lists with the corresponding values from the list of dictionaries (students)?

for i in range(100):
    first_names.append(students[i]['first_name'])
    last_names.append(students[i]['last_name'])
    addresses.append(students[i]['address'])
    maths_grades.append(students[i]['maths'])
    linguistics_grades.append(students[i]['linguistics'])
    psychology_grades.append(students[i]['psychology'])

# Now, can you turn this dataset into a pandas dataframe?
#   hint: use the list of dictionaries to initialize your dataframe

import pandas
students_df = pandas.DataFrame(students)

# What if you wanted to create a 3x100 numpy array of all the grades? (excluding the other information)
#   hint: use the separate lists to create a list of lists to initialize your array

students_grades_only = [maths_grades, linguistics_grades, psychology_grades]
students_grades_only_arr = np.array(students_grades_only)


# Now, try to do the following for all four data structures: list of dictionaries, separate lists, dataframe, array.
# Don't spend more than 20 minutes on any of these!
# Thinking about a solution is more important than actually programming it.
# 1. Get all the information belonging to the 20th student
# 2. Find the student with the highest linguistics grade
# 3. Calculate the average grade per student; (maths + linguistics + psychology) / 3
# What operations do you find easier to do in each of these four structures? And what operations harder?

# list of dictionaries
# 1.
print(students[19])
# 2.
for i in range(100):
    if students[i]["linguistics"] == max(linguistics_grades):
        print(students[i]['first_name'])
# 3.
average_grade_a = []
for i in range(100):
    average_grade_a.append((students[i]["maths"] + students[i]["linguistics"] + students[i]["psychology"])/3)

# separate lists
# 1.
print(first_names[19], last_names[19], addresses[19], maths_grades[19], linguistics_grades[19],psychology_grades[19])
# 2. (only the first student with the max. grade)
index = linguistics_grades.index(max(linguistics_grades))
name = first_names[index]
print(name)
# 3.
average_grade_b = []
for i in range(100):
    average_grade_b.append((maths_grades[i] + linguistics_grades[i] + psychology_grades[i])/3)

# dataframe
# 1.
print(students_df.loc[19])
# 2.
print(students_df.loc[students_df['linguistics'] == max(linguistics_grades), 'first_name'])
# 3.
average_grade_c = []
for i in range(100):
    average_grade_c.append((students_df['linguistics'][i] + students_df['maths'][i] + students_df['psychology'][i])/3)


# arrays
students_array = np.array([first_names, last_names, addresses, maths_grades, linguistics_grades, psychology_grades])
# 1.
print(students_array[:,19])
# 2.
print(np.where(students_array == max(students_array[4,:]))) # in my example of the fake data 2x max found in column 4, getting row index from 2nd output array
print(students_array[0,1])
print(students_array[0,95])
# 3.
average_grade_d = []
for i in range(100):
    average_grade_d.append(students_grades_only_arr.mean(axis=1))
    # not sure why I get different averages here than with the other data types?


# In general, I find dataframes and arrays easier to work with
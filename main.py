# Squaring The Numbers

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)

# Filtering Even Numbers

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# Data Over Lap

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()

# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
# result = [num for num in file_1_data if num in file_2_data]
#
# print(result)

# Dictionary Comprehension Practice - 1

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# import random

# names = ["Akash", "Bhushan", "Chandra", "Dheeraj", "Elankar", "Farook"]
# students_score = {student:random.randint(1, 100) for student in names}
# passed_students = {student:score for (student, score) in students_score.items() if score >= 68}

# Dictionary Comprehension Practice-2

# sentence = "What Is The Air Speed Velocity Of An Unladen Swallow ?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# Dictionary Comprehension Practice-3

# weather_c = {
#     "MonDay": 12,
#     "TuesDay": 14,
#     "WednesDay": 15,
#     "ThursDay": 14,
#     "FriDay": 21,
#     "SaturDay": 22,
#     "SunDay": 24
# }

# weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# Iteration Of Pandas Data Frame
# student_dict = {
#     "student": ["Rama", "Bharata", "Lakshmana", "Shatrughn"],
#     "score": [90, 80, 70, 60]
# }

# Looping Through Dictionaries

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# # Looping Through A Data Frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)
#
# # Loop Through Rows Of A Data Frame
# for (index, row) in student_data_frame.iterrows():
#     # print(index)
#     # print(row)
#     # print(row.student)
#     # print(row.score)
#     if row.student == "rama":
#         print(row.score)

# NATO Alphabet Project...

# # Looping Through Dictinaries:
# for (key, value) in student_dict.items():
#     # Access Key And Values
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop Through Rows Of A Data Frame:
# for (index, row) in student_data_frame.iterrows():
#     # Access Index And Row
#     # Access row.student or row.score
#     pass

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

word = input("Enter A Word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)


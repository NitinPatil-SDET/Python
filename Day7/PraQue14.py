#2 Student marks Dictionnary
#create dict if student, add a nem student, update mark of exiting student

student = { "student1": {"name": "Halku", "marks":86},
            "student2": {"name": "spidy", "marks":55},
            "student3": {"name": "Ironman", "marks":76},
            "student4": {"name": "Adarak", "marks":95}               
        }

print("Intial value of Students", student) 

#add a nem student
student.update({"student5": {"name": "Santra", "marks":67}  })
print("After adding new Students", student) 

#update mark of exiting student
student.update({"student2": {"name": "spidy", "marks":99}  })
print("After spidy get grace: ", student)
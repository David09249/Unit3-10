# Created by : David Wang
# Created on : 27 Oct 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-10
# This program calculates the average of your grade(s)

# constants
grades = []
print('Enter a number from 0-100. Enter -1 to end.')
while True:
    try:
        
        # input
        grade = raw_input()
        grade = float(grade)
        if grade >= 0:
            if grade <= 100:
                grade_average = float(0)
                grades.append(grade)
                for index in range(0, len(grades)):
                
                # process
                    grade_average = grade_average + grades[index]
                grade_average = grade_average / len(grades)
                
                # output
                print("Your grades are: " + str(grades) + "\nYour average is: " + str(grade_average))
            else:
                print('Please enter a grade from 0-100 or enter -1 to end.')
        else:
            print('Ended')
            break
    except:
        print('Please enter a valid grade.')

#! /usr/bin/env python3
MESSAGE1 = 'Your letter grade is a'
MESSAGE2 = 'Your letter grade is an'
print('What is your percentage of correct answers?')
connection = float(input())
if connection >100:
    print("YOU LIED!!!")
elif connection >= 90:
    MESSAGE2 = MESSAGE2 + " A!!"
    print(MESSAGE2)
elif connection >= 80:
    MESSAGE1 = MESSAGE1 + " B!!"
    print(MESSAGE1)
elif connection >= 70:
    MESSAGE1 = MESSAGE1 + " C!!"
    print(MESSAGE1)
elif connection >= 60:
    MESSAGE1 = MESSAGE1 + " D!!"
    print(MESSAGE1)
elif connection <= 59:
    MESSAGE1 = MESSAGE1 + " F!!"
    print(MESSAGE1)
print("end of script")

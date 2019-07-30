#! /usr/bin/env python3
message1 = 'Your letter grade is a'
print('What is your percentage of correct answers?')
connection = float(input())
if connection >100:
    message1 = message1 + " You LIE!!!"
elif connection >= 90:
    message1 = message1 + " A, congrats!!"
elif connection >= 80:
    message1 = message1 + " B, try a little harder next time!!"
elif connection >= 70:
    message1 = message1 + " C, average Joe!!"
elif connection >= 60:
    message1 = message1 + " D, get studying!!"
elif connection <= 59:
    message1 = message1 + " F, You FAILED"
print(message1)
print("end of script")

#! /usr/bin/env python3

round = 0
while(True):
    round = round + 1
    print('Finish the movie title. "Monty Python\'s The Life of ______"')
    answer = input()
    answer2 = answer.lower()
    if (answer == 'Brian'):
        print('Correct')
        break
    elif (answer2 == 'brian'):
        print('Correct')
        break
    elif(round==3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry, Try again')


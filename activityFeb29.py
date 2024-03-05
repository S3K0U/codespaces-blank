#The python that make statements like (IF/ELSE) try to work is something called the logistic statement because yjey also do the try if itd less than 30 they need to restart

def wasHighscoreReached():
    userScore = int(input('what is your score?'))
    if userScore > 3000:
        print('Congrats! You have the high score!')
    else:
        print ('You did not reach the high score. Try again.')

        wasHighscoreReached
from random import randint

num = randint(0, 10)
# print(num)
ct = 0

while ct < 3:

    try:
        guess = int(input('enter a number between 0 to 10:'))
        if guess == num:
            print('You Got it!')
            break
        else:
            if ct == 2:
                print('You Lose')
            else:
                print('You have guessed wrong number')
                print('Try Again')

    except:
        print('Kindly enter a num between 0 and 10')
    ct += 1
    print(f'You have guessed {ct} time(s)')
print('/// Game Finished')
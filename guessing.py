import random 
def guess(x):
    random_number=int(random.randint(1,x))
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}'))
        if guess>random_number:
            print('Too high')
        elif guess<random_number:
            print('Too low')
    print(f"You've guessed the number {random_number} correctly! ")
            
guess(10)
            


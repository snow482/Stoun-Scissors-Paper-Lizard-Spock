from random import randint
rand_num = randint(0,5)

if rand_num == 0:
    comp = 'rock'
elif rand_num == 1:
    comp = 'scissors'
elif rand_num == 2:
    comp = 'paper'
elif rand_num == 3:
    comp = 'lizard'
else:
    comp = 'spock'

p2 = input('player move:\n').lower()
print(f'comp - {comp}\n')

if comp == p2:
    print('tie')
elif p2 == 'rock':
    if comp == 'scissors':
        print('player wins - rock crushed scissors')
    elif comp == 'lizard':
        print('player wins - rock crushed lizard')
    else:
        print('comp wins')

elif p2 == 'scissors':
    if comp == 'paper':
        print('player wins - scissors cut paper')
    elif comp == 'lizard':
        print('player wins - scissors dicupitates lizard')
    else:
        print('comp wins')

elif p2 == 'paper':
    if comp == 'rock':
        print('player wins - paper covers rock')
    elif comp == 'spock':
        print('player wins - paper disproves spock')
    else:
        print('comp wins')

elif p2 == 'lizard':
    if comp == 'spock':
        print('player wins - lizard poisons Spock')
    elif comp == 'paper':
        print('player wins - lizard eats Paper')
    else:
        print('comp wins')

elif p2 == 'spock':
    if comp == 'scissors':
        print('player wins - spock smashes scissors')
    elif comp == 'rock':
        print('player wins - spock vapourises rock')
    else:
        print('comp wins')

else:
    print('please, enter a valid move')



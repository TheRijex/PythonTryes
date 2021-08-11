import random
should_cont = True

while should_cont:
    player_choise = input('Player choise is Paper or Stone or Scissors?').lower()

    if player_choise not in ['paper', 'stone', 'scissors']:
        print('Error')
        continue
    gen = {1:'paper',2:'stone', 3:'scissors'}
    comp_choise = gen[random.randint(1, 3)]

    print(f'Comp choise is {comp_choise}')

    wining_combinations = [('stone', 'scissors'),('paper', 'stone'),('scissors','paper')]

    if player_choise == comp_choise:
        print('A draw')
    elif (player_choise, comp_choise) in wining_combinations:
        print('You win')
    else:
        print('Comp wins')

    should_cont = input('Want to proceed?').lower() == 'yes' 
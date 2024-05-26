import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

#value = roll()
#print(value)

while True:
    players = input('Enter the number of players(2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Invalid try again')

#print(players)

MAX_SCORE = 50
PLAYER_SCORES = [0 for _ in range(players)] 

print(PLAYER_SCORES)

while max(PLAYER_SCORES) < MAX_SCORE:
    
    for player_index in range(players):
        print('\nPlayer number', player_index + 1, 'turn  has just started!\n')
        current_score = 0
     
        while True:
            should_roll = input('Would you like to roll?: (y) ')
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1 turn is over")
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a: {value}')

            print(f'your current score is, {current_score}')

    PLAYER_SCORES[player_index] += current_score
    print(f'your total score is: {PLAYER_SCORES[player_index]}')
            
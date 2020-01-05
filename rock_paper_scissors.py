# Rock Paper Scissors Game
player1_score = 0
player2_score = 0


print('.....ROCK.....')
print('....PAPER.....')
print('...SCISSORS...')
print('..............')

#player1 input
player1_input = input('SHOOT!  -> ')
#player2 input
player2_input = input('SHOOT!  -> ')
#result

if player1_input == 'rock':
    if player2_input == 'rock':
        print('draw')
    elif player2_input == 'paper':
        print('paper covers rock')
        player2_score += 1
    elif player2_input == 'scissors':
        print('rock smashes scissors')
        player1_score += 1
elif player1_input == 'paper':
    if player2_input == 'paper':
        print('draw')
    elif player2_input == 'rock':
        print('paper covers rock')
        player1_score += 1
    elif player2_input == 'scissors':
        print('scissors cut paper')
        player2_score += 1
elif player1_input == 'scissors':
    if player2_input == 'scissors':
        print('draw')
    elif player2_input == 'rock':
        print('rock smashes scissors')
        player2_score += 1
    elif player2_input == 'paper':
        print('scissors cut paper')
        player1_score += 1

print(f'Player1 score: {player1_score}')
print(f'Player2 score: {player2_score}')
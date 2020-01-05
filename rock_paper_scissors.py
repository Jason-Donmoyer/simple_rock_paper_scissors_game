# Rock Paper Scissors Game
import random

player1_score = 0
player2_score = 0
game = True
round = 1


while game:

    print(f'ROUND {round}')
    print('.....ROCK.....')
    print('....PAPER.....')
    print('...SCISSORS...')
    print('..............')

    #player1 input
    player1_input = input('SHOOT!  -> ')
    if player1_input != 'rock':
        if player1_input != 'paper':
            if player1_input != 'scissors':
                print('Please enter a valid input!!!')
                player1_input = input('SHOOT!  -> ')
    #player2 input
    # player2_input = input('SHOOT!  -> ')
    # if player2_input != 'rock':
    #     if player2_input != 'paper':
    #         if player2_input != 'scissors':
    #             print('Please enter a valid input!!!')
    #             player2_input = input('SHOOT!  -> ')
    #player2 AI input
    random_num = random.randint(1,3)
    if random_num == 1:
        player2_input = 'rock'
    elif random_num == 2:
        player2_input = 'paper'
    elif random_num == 3:
        player2_input = 'scissors'

    print(f'Player2 shoots {player2_input}!')
    #result logic

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

    #print scores
    print(f'Player1 score: {player1_score}')
    print(f'Player2 score: {player2_score}')

    if player1_score > player2_score:
        print('Player1 is in the lead!!')
    elif player1_score < player2_score:
        print('The AI is ahead!')
    elif player1_score == player2_score:
        print('All tied up!')

    #new round or quit
    playAgain = input("Play again? Y/N")
    if playAgain == 'Y' or playAgain == 'y':
        game = True
        round += 1
    else:
        game = False


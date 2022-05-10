import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of game results
wins = 0
losses = 0
ties = 0

# Main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    # Player input loop
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

        player_move = input()
        if player_move == 'q':
            sys.exit()  # quit

        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break

        print('Type one of r, p, s, or q')

    # Display player move
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display computer move
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computer_move = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computer_move = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record win/loss/ties
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == 'r' and computer_move == 's' or \
            player_move == 'p' and computer_move == 'r' or \
            player_move == 's' and computer_move == 'p':
        print('You win!')
        wins += 1
    elif computer_move == 'r' and player_move == 's' or \
            computer_move == 'p' and player_move == 'r' or \
            computer_move == 's' and player_move == 'p':
        print('Computer wins!')
        losses += 1

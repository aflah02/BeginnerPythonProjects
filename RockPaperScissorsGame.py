import random
ls = ['Rock', 'Paper', 'Scissors']
while True:
    k = int(input("How Many Times do You Want to Play?"))
    player_score = 0
    comp_score = 0
    for i in range(k):
        comp_choice = random.choice(ls)
        print(comp_choice)
        player_choice = input("Choose one of Rock, Paper or Scissors")
        if comp_choice == 'Rock':
            if player_choice == 'Paper':
                print('Player Wins')
                player_score = player_score + 1
            elif player_score == 'Scissors':
                print('Computer Wins')
                comp_score = comp_score + 1
            elif player_score == 'Rock':
                print('Tie')
        elif comp_choice == 'Paper':
            if player_choice == 'Scissors':
                print('Player Wins')
                player_score = player_score + 1
            elif player_score == 'Rock':
                print('Computer Wins')
                comp_score = comp_score + 1
            elif player_score == 'Paper':
                print('Tie')
        elif comp_choice == 'Scissors':
            if player_choice == 'Rock':
                print('Player Wins')
                player_score = player_score + 1
            elif player_score == 'Paper':
                print('Computer Wins')
                comp_score = comp_score + 1
            elif player_score == 'Scissors':
                print('Tie')
    if comp_score > player_score:
        print(f'Computer Won by {comp_score - player_score} points')
    elif player_score > comp_score:
        print(f'Player Won by {player_score - comp_score} points')
    else:
        print('It was a Draw')
    ask = input('Do you want to play again? (y/n)')
    if ask == 'n':
        print('Thank You for Playing! Have Fun')
        break

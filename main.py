from art import Board
import time
answer = input('Hey mister, want to play a game of TIC TAC TOE???\nType "yes" or "no".\n')


def tictactoe():

    def game(player, opp):
        is_on = True
        board = Board()
        print(f"Very well, let us begin:")
        board.print_board()
        while is_on:
            if len(board.filled_spots) == 9 and not board.win_check(player=player, opp=opp):
                print('Y\'all done drawed. Ain\'t no point continuin\', now.')
                is_on = False
            else:
                move = input(f'Where would you like to place an {player}?\nType the coordinates ("B2", "A3", etc)\n').upper()
                board.move(input=move, player=player)
                time.sleep(.70)
                if board.win_check(player=player, opp=opp):
                    is_on = False
                else:
                    print('\nNow its opp\'s turn...\n')
                    board.opp(opp)
                    print('\n')
        again = input('Can you piss off, or are we going to do this all over again?\n("Y" to play again, "N" to exit).').upper()
        if again == 'Y':
            tictactoe()
        else:
            print('Thank god, now BUZZ OFF!!!')
            exit()

    answer = input('Would you like to play as "X\'s" or "O\'s"? Type "X" or "O":\n').upper()
    if answer == 'X':
        player = 'X'
        opp = 'O'
        game(player, opp)
    elif answer == 'O':
        player = 'O'
        opp = 'X'
        game(player, opp)
    else:
        print('Not a chance, bub. Try again.')
        tictactoe()


if answer == 'yes':
    tictactoe()
#     place game func here
else:
    print('Ok, then why did you launch the program that literally only does Tic Tac TOE?')

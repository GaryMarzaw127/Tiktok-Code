import random

def play():
    user = input("apa pilihan mu ? \n'b' untuk BATU, \n'k' untuk KERTAS, \n'g' untuk GUNTING\n\n : ")
    computer = random.choice(['b','k','g'])

    print('\n')
    print(f'user : {user} vs {computer} : computer')

    if user == computer:
        return 'seri'

    if is_win(user,computer):
        return 'kamu menang !'

    print('\n')
    return 'kamu kalah !'

def is_win(player,lawan):
    if(player == 'b' and lawan == 'g') or (player == 'g' and lawan == 'k') or (player == 'k' and lawan == 'b'):
        return True
    
    
print(play())


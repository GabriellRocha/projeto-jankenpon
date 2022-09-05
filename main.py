from random import randint
from ascii import rock, paper, scissors


game_imagem = [rock, paper, scissors]
user_choice = int(input('Qual você escolhe? 0 para pedra, 1 para papel ou 2 para tesoura\n'))

if user_choice >= 3 or user_choice < 0:
    print('Você escolheu um número inválido. Você perdeu!')
else:
    print('Você')
    print(game_imagem[user_choice])
    computador_chose = randint(0, 2)
    print('Computador:')
    print(game_imagem[computador_chose])
    if user_choice == 0 and computador_chose == 2:
        print('Você venceu!')
    elif computador_chose == 0 and user_choice == 2:
        print('Você perdeu!')
    elif user_choice > computador_chose:
        print('Você venceu!')
    elif computador_chose > user_choice:
        print('Você perdeu!')
    elif computador_chose == user_choice:
        print('Empate')

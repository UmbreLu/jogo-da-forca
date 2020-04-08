#! python3
from random import randint



def input_h1():
    while True:
        rawup = input('Escolha uma letra: ').upper()
        if len(rawup) == 1 and rawup.isalpha() and not rawup in display and not rawup in wrong_letters and not rawup in letras_certas:
            return rawup
        else:
            print('Entrada inválida. Por favor, tente apenas letras que você não tentou antes.\n')

def input_h2():
    while True:
        rawup = input('<sim/não> ').upper()
        if rawup == 'SIM' or rawup == 'NÃO' or rawup == 'NAO':
            return rawup
        else:
            print('Entrada inválida. Use apenas "sim" ou "não".')

# random word picker
def r_word(wordbankfile='words_pt.txt'):
    with open(wordbankfile, 'r') as f:
        word_list = f.readlines()
        striped_list = []
        for line in word_list:
            striped_list.append(line.strip())
    size = len(striped_list)
    return striped_list[randint(0, (len(word_list) - 1))]


def drawgame():
    show_display = ' '.join(display)
    hangman_dict = {6:r'''
 _____ 
|    $ 
|   /|\
|   / \ ''', 5:r'''
 _____ 
|    0 
|   /|\
|    |  ''', 4:r'''
 _____ 
|    0 
|   /|\
|       ''', 3:r'''
 _____ 
|    0 
|   / \
|       ''', 2:'''
 _____ 
|    0 
|    | 
|       ''', 1:'''
 _____ 
|    0 
|      
|       ''', 0:'''
 _____ 
|      
|      
|       '''}
    print(hangman_dict[to_hang] + 'Palavra Secreta: ' + show_display + '\n' + message + '\n')
    


# global scope -----------------------
print('''
===================================================
         Bem-vindo(a) ao Jogo da Forca!
===================================================

    Tente adivinhar a palavra secreta escolhendo letra
por letra. Mas tenha cuidado, pois se indicar 6
letras que não estejam na palavra secreta, você
perderá!

    Obs.: Existem muitas palavras compostas no banco de
palavras. Para facilitar elas já virão com um "-"
visível.''')

acentos = {'A':{'A', 'Á', 'Â', 'Ã'}, 'E': {'E', 'É', 'Ê'}, 'I': {'I', 'Í'}, 'O': {'O', 'Ó', 'Ô', 'õ'}, 'U': {'U', 'Ú'}, 'C': {'C', 'Ç'}}

still_playing = True
while still_playing:
    
    word = r_word()
    display = ['_']*len(word)
    to_hang = 0
    wrong_letters = []
    letras_certas = []
    message = ''
    index2 = 0
    for letter in word:
        if letter == '-':
            display[index2] = '-'
        index2 += 1

    drawgame()

    player_not_won = True
    player_not_dead = True
    while (player_not_won and player_not_dead):

        player_input = input_h1()
        tá_sim = False
        message = ''
        if player_input in acentos.keys():
            player_mod = acentos[player_input]
        else:
            player_mod = player_input
        for player_letter in player_mod: # player_letter pode ser um set, então é necessário um for loop
            if player_letter in word:
                tá_sim = True
                index = 0
                for letter in word:
                    if letter == player_letter:
                        display[index] = player_letter
                        message += f'Ótimo! A letra "{player_letter}" está correta.\n'
                        if not player_input in letras_certas:
                            letras_certas.append(player_input)
                    index += 1

        if not tá_sim:
            to_hang += 1
            wrong_letters.append(player_input)
            message = f'A letra "{player_input}" não existe na palavra secreta.'

        drawgame()

        if to_hang >= 6:
            player_not_dead = False
            print('Sinto muito, mas você indicou 6 letras que não estavam')
            print('na palavra secreta e perdeu.')
            print('Letras incorretas: ' + ', '.join(wrong_letters) + '.')
            print(f'A palavra secreta era "{word}".')

        if ''.join(display) == word:
            player_not_won = False
            print(f'Parabéns! Você acertou a palavra secreta, que era "{word}".')


    print('\n\n\nDeseja jogar novamente?')
    if input_h2() == 'SIM':
        pass
    else:
        still_playing = False

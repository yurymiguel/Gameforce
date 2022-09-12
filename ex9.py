import random
def word(f):
    file = open(f,'r')
    words = file.read()
    global aleatory
    aleatory = random.choice(words.lower().split())
    return aleatory

def game():
    print('Agora vamos começar nossa Forca\nVocê possui 6 chances de acertar a palavra!!!\nVaaaleendooo')
    a = 7
    global user
    w = []
    stop = [x for x in aleatory]
    while not a == 0:
        user = input('Digite uma Letra: ')

        if user in aleatory:
            w.append(user)
            print('Você acertou a letra')
            if stop == w:
                print('Parabéns você acertou a palavra!!!')
                break

        elif a == 1:
            print('Você perdeu todas suas chances')
            break

        else:
            a-=1
            print(f'Ops Letra Errada, chances ---> {a}')


if __name__ == '__main__':

    word('aleatory_words')
    game()





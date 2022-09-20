
def char(char):
    while True:
        try:
            char = input(char)
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return char

def principal(msg):
    print('='*50)
    print(msg.center(50))
    print('='*50)




def leiaint(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mDigite um valor válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return n

def leiafloat(f):
    while True:
        try:
            f = float(input(f))
        except (ValueError,TypeError):
            print('\033[31mDigite um valor válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return f


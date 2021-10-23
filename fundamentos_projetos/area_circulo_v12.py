#!/usr/local/bin/python3
from math import pi
import sys
import errno
def circulo(raio):
    return pi * float(raio) ** 2

def help():
    print(f"""\
        É necessário informar o raio do círculo.
        Sintaxe: {sys.argv[0]} <raio> """)


if __name__ == '__main__':
    if len(sys.argv) <2:
        help()
        # exit(errno.EPERM)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Àrea do círculo', area)

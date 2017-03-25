# coding=UTF-8

import time
texto=open("texto.txt","r")
import sys
import os

print(chr(27) + "[2J")
print('\r')


def delay_print(s):
        for c in s:
            sys.stdout.write( '%s' % c )
            sys.stdout.flush()
            time.sleep(0.1)
print("Iniciando")

time.sleep(2)


print("Cargando datos")

time.sleep(0.5)

print("3")

time.sleep(0.5)

print("2")

time.sleep(0.5)

print("1")

time.sleep(0.5)

#pirint("\n"*50)
print(chr(27) + "[2J")
print('\r')
sys.stdout.flush()
time.sleep(2)

for i in texto:

    delay_print(i)
    time.sleep(1.5)
os.system("~/space-invaders")

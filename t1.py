# coding=UTF-8

import time
texto=open("texto.txt","r")
import sys

def delay_print(s):
        for c in s:
            sys.stdout.write( '%s' % c )
            sys.stdout.flush()
            time.sleep(0.25)
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

print("\n"*100)

time.sleep(4)

for i in texto:
    delay_print(i)


    print("\n")
    time.sleep(1.5)

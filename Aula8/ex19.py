#sorteando um item na lista
import random
no1 = input("Primeiro nome: ")
no2 = input('Segundo nome: ')
no3 = input("terceiro nome: ")
no4 = input('Quarto nome: ')
lista = [no1, no2, no3, no4]
escolhido = random.choice(lista)
print(" o nome sorteado foi {} ".format(escolhido))

#Segunda forma de fazer

from random import choice
no1 = input("Primeiro nome: ")
no2 = input('Segundo nome: ')
no3 = input("terceiro nome: ")
no4 = input('Quarto nome: ')
lista = [no1, no2, no3, no4]
escolhido = choice(lista)
print(" o nome sorteado foi {} ".format(escolhido))
import os
import random
import string
import time

os.system('cls||clear')

print('ESCOLHA'
     '\n')

while True:
  D = int(input('QUAL A DIFICULDADE? (4-10) '))
  if D>= 4 and D<= 10:
    break

M = ''

for i in range(D):
  M += random.choice(string.ascii_uppercase)

os.system('cls||clear')

print('DIGITE ESSA MENSAGEM:'
      '\n'
      '\n', M)

time.sleep(0.5*D)

os.system('cls||clear')

N = input('').upper()

if N == M:
  print('MENSAGEM CORRETA'
       '\n''VOCÊ GANHOU!'
       '\n')

else:
  print('VOCÊ ENTENDEU ERRADO'
       '\n''VOCÊ DEVERIA TER ENVIADO: ', M)
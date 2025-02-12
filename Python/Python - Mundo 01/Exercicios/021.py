# Exercício 21 - Faça um progama em Python que abra e reproduza o áudio 
# de um arquivo MP3.


# Importando a biblioteca "import ...".
import os 
import pygame  # type: ignore

# "os.system('cls')" = limpa o terminal | 
os.system('cls')


# Pular linha "\n"
print("\n")


pygame.mixer.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()

# Pular linha "\n"
print("\n")

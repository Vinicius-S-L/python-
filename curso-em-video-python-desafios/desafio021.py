import time
import keyboard
import pygame


pygame.mixer.init()
pygame.mixer.music.load('C:/Users/Família\Documents/DOCUMENTOS/vinicius/curso-em-video-python-desafios/Colossenses e suas linhas de amor - Fhop Music & Marco Telles ｜ cover Regenerados 🪴.mp3')
pygame.mixer.music.play()

pause = False

while True:
    if keyboard.is_pressed('space'):
        if not pause:
            pygame.mixer.music.pause()
            pause = True
            print('pausado')
        else:
            pygame.mixer.music.unpause()
            pause = False
            print('iniciado')

        time.sleep(1)

    if keyboard.is_pressed('r'):
        pygame.mixer.music.play()
        pause = False







"""keyboard.read_key() == 'space':
    pygame.mixer.music.get_busy() == True:
    pygame.event.wait()
if keyboard.read_key() == 'space' and pygame.mixer.music.play() == False:
    pygame.mixer.music.play()
    time.sleep(2)"""


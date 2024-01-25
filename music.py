import pygame
import os

pygame.init()
global volume


def change_volume(volume):
    pygame.mixer.music.set_volume(volume)


def music(volume=1.0):
    music_folder = 'music/'
    music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

    pygame.mixer.init()

    for music_file in music_files:
        music_path = os.path.join(music_folder, music_file)
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=-1)

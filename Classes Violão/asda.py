
def tocar(self):
    x = str(input('Qual corda você quer torcar ? '))
    if x == ('mi maior') or x == ('mimaior'):
        import pygame
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('Mimaior.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        pygame.event.wait()
        print(type(x))


tocar('violao')
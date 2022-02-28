class Violao:
    def __init__(self, tipocordas, tom, tamanho, cor, marca):
        self.tipocordas = tipocordas
        self.tom = tom
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca

    def tocar(self):
        x = str(input('Qual corda você quer torcar ? '))
        if x == ('mi maior') or x == ('mimaior'):
            import pygame
            pygame.mixer.init()
            pygame.init()
            pygame.mixer.music.load('Mimaior.mp3')
            pygame.mixer.music.play(loops=0, start=0.0)
            pygame.event.wait()

        elif x == ('mi menor') or x == ('mimenor'):
            import pygame
            pygame.mixer.init()
            pygame.init()
            pygame.mixer.music.load('Mimenor.mp3')
            pygame.mixer.music.play(loops=0, start=0.0)
            pygame.event.wait()
        elif x == ('Re') or x == ('re'):
            import pygame
            pygame.mixer.init()
            pygame.init()
            pygame.mixer.music.load('Re.mp3')
            pygame.mixer.music.play(loops=0, start=0.0)
            pygame.event.wait()
        elif x == ('La') or x == ('la'):
            import pygame
            pygame.mixer.init()
            pygame.init()
            pygame.mixer.music.load('La.mp3')
            pygame.mixer.music.play(loops=0, start=0.0)
            pygame.event.wait()
        elif x == ('Si') or x == ('si'):
            import pygame
            pygame.mixer.init()
            pygame.init()
            pygame.mixer.music.load('La.mp3')
            pygame.mixer.music.play(loops=0, start=0.0)
            pygame.event.wait()
        elif x == ('Sol') or x == ('sol'):
            import pygame
            pygame.mixer.init()
            pygame.init()
            pygame.mixer.music.load('Sol.mp3')
            pygame.mixer.music.play(loops=0, start=0.0)
            pygame.event.wait()

    pass


violao1 = Violao('Cordas de nylon', 'Grave', '103,4 cm', 'preto', 'Austin')
violao1.tocar()

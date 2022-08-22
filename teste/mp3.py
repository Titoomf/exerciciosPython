    import pygame

    pygame.init()
    pygame.mixer.music.load('tito.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(300000)
    pygame.event.wait()

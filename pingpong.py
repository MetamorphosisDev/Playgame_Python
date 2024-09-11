#create a Pingpong game!
import random
from pygame import *


class GameSprite():
    def __init__(self, image_path, image_size, x, y, speed_x, speed_y):
        self.image = transform.scale(image.load(image_path), image_size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def l_update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < window_size[1] - self.image.get_height():
            self.rect.y += self.speed_y
    
    def r_update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < window_size[1] - self.image.get_height():
            self.rect.y += self.speed_y
    
    def update(self):
        global inactive

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x < 0:
            inactive = True
            window.blit(r_win, r_win.get_rect(center=(window_size[0]/2, window_size[1]/2)))
        elif self.rect.x > window_size[0] - self.image.get_width():
            inactive = True
            window.blit(l_win, l_win.get_rect(center=(window_size[0]/2, window_size[1]/2)))

        if self.rect.y > window_size[1] - self.image.get_height() or self.rect.y < 0:
            self.speed_y *= -1

        if self.rect.colliderect(l_racket.rect) or self.rect.colliderect(r_racket.rect):
            self.speed_x *= -1

            #Speed
            self.speed_x = random.uniform(2, 7) * (1 if self.speed_x > 0 else -1)
            self.speed_y = random.uniform(2, 7) * (1 if self.speed_y > 0 else -1)

back = (200, 255, 255) # warna background
window_size = (600, 500) # (width, height)
window = display.set_mode(window_size)
display.set_caption('Ping-Pong')

clock = time.Clock()
FPS = 60

# font
font.init()
font = font.Font(None, 70)
l_win = font.render('LEFT PLAYER WIN', True, (255, 215, 0))
r_win = font.render('RIGHT PLAYER WIN', True, (255, 215, 0))

# sprite
racket_size = (50, 150)
ball_size = (50, 50)
l_racket = Player('racket.png', racket_size, 30, 200, 4, 4)
r_racket = Player('racket.png', racket_size, 520, 200, 4, 4)
ball = Player('tenis_ball.png', ball_size, 200, 200, 2, 2)


game = True
inactive = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if not inactive:
        window.fill(back)
        l_racket.reset()
        r_racket.reset()
        ball.reset()

        # if hero.rect.colliderect(enemy.rect):
        #     window.blit(lose, lose.get_rect(center=(window_size[0]/2, window_size[1]/2)))
        #     kick.play
        #     inactive = True

        # if hero.rect.colliderect(treasure.rect):
        #     window.blit(win, lose.get_rect(center=(window_size[0]/2, window_size[1]/2)))
        #     money.play()
        #     inactive = True
        
        l_racket.l_update()
        r_racket.r_update()
        ball.update()
    
    display.update()
    clock.tick(FPS)
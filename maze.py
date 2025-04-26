#создай игру "Лабиринт"!
from pygame import *
from time import sleep
class GameSprite(sprite.Sprite):
    def __init__(self,imagename,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(imagename),(60,60))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,x,y,height,width):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width,self.height))
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Hero(GameSprite):
    def update(self):
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x == 600:
            self.direction = "left"
        if self.rect.x == 450:
            self.direction = "right"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        

window = display.set_mode((700,500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.jpg"),(700,500))
clock = time.Clock()
fps = 60

font.init()
font = font.Font(None,70)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

vovasoladkov = Hero("hero.png",20,20,11)
popka = Enemy("cyborg.png",600,300,10)
jopka = Enemy("lukas.png",600,100,10)
goldgoldgold = GameSprite("treasure.png",600,401,0)
titikaka1 = Wall(202,60,182,0,250,350,30)
titikaka2 = Wall(255,50,48,100,0,350,30)
titikaka3 = Wall(9,1,55,200,250,350,30)

titikaka4 = Wall(228,76,42,300,0,350,30)
titikaka5 = Wall(1,42,156,400,250,350,30)


game = True
while game:
    key_pressed = key.get_pressed()
    window.blit(background,(0,0))
    titikaka1.draw_wall()
    titikaka2.draw_wall()
    titikaka3.draw_wall()
    titikaka4.draw_wall()
    titikaka5.draw_wall()
    vovasoladkov.draw()
    vovasoladkov.update()
    popka.draw()
    popka.update()
    jopka.draw()
    jopka.update()
    goldgoldgold.draw()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(vovasoladkov,titikaka1) or sprite.collide_rect(vovasoladkov,titikaka2) or sprite.collide_rect(vovasoladkov,titikaka3) or sprite.collide_rect(vovasoladkov,titikaka4) or sprite.collide_rect(vovasoladkov,titikaka5):
            vovasoladkov.rect.x = 0
            vovasoladkov.rect.y = 10
    if sprite.collide_rect(vovasoladkov,popka):
            lose_label = font.render("ХАХАХАХАААХАХАХ", True, (0,255,0))
            window.blit(lose_label,(200,250))
            display.update()
            time.delay(3000)
            game = False
    if sprite.collide_rect(vovasoladkov,jopka):
            lose_label = font.render("ХАХАХАХАААХАХАХ", True, (0,255,0))
            window.blit(lose_label,(200,250))
            display.update()
            time.delay(3000)
            game = False
    if sprite.collide_rect(vovasoladkov,goldgoldgold):
            lose_label = font.render("УРААААААААААААААААААААА", True, (0,255,0))
            window.blit(lose_label,(200,250))
            display.update()
            time.delay(3000)
            game = False
    display.update()
    clock.tick(fps)
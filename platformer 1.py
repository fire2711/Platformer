import pygame
from settings import *
from os import path


pygame.init()
pygame.display.set_caption("Platformer")


screen_width = 1000
screen_height = 1000
tile_size = 50
main_menu = True
blue = (100, 0, 200)
font = pygame.font.SysFont('Bauhaus 93', 70)

SCREEN = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

# images
BG = pygame.image.load("images/bluemoon.png")
menu = pygame.image.load("images/desert-21.png")
main_menuimage = pygame.transform.scale(menu, (screen_width, screen_height))
scale = pygame.transform.scale(BG, (screen_width, screen_height))
start = pygame.image.load("images/start_btn.png")
exit = pygame.image.load("images/exit_btn.png")


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y)) 

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked = False
        SCREEN.blit(self.image, self.rect)
        return action



class Level():
    def __init__(self,data):
        self.list = []
        cloud = pygame.image.load("images/brick.jpg")

        rowcount = 0
        for row in data:
            colcount = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(cloud, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = colcount * tile_size
                    img_rect.y = rowcount * tile_size
                    tile = (img, img_rect)
                    self.list.append(tile)
                colcount += 1
            rowcount +=1
    def create(self):
        for tile in self.list:
            SCREEN.blit(tile[0],tile[1])
            # pygame.draw.rect(SCREEN, (255, 255, 255), tile[1], 2)
                    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y ):
        img = pygame.image.load("images/blob.png")
        self.image = pygame.transform.scale(img, (25,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 5
        self.jump = 0
        self.jumped = False

        
    
    def appgravity(self):
        self.direction.y = 5
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed

        self.rect.y -= self.direction.y

    def update(self):
        # keypresses
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if keys[pygame.K_RIGHT]:
                dx += 5
        if keys[pygame.K_LEFT]:
                dx -= 5
        if keys[pygame.K_SPACE] and self.jumped == False:
            self.jump = -15
            self.jumped = True
        # if keys[pygame.K_SPACE] == False:
        #     self.jumped = False
        # gravity
        self.jump += 1
        if self.jump > 10:
            self.jump = 10
        dy += self.jump

        # collision
        for tile in level.list:
            # x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # y directions
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.jump < 0:
                    dy = tile[1].bottom - self.rect.top
                if self.jump >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.jumped = False
            
            

        self.rect.x += dx
        self.rect.y += dy

        SCREEN.blit(self.image, self.rect)
        # pygame.draw.rect(SCREEN, (255, 255, 255), self.rect, 2)
        

player = Player(100 , screen_height -  75)
level = Level(data)
start_but = Button(screen_width //2 -350, screen_height //2, start)
exit_but = Button(screen_width //2 +50, screen_height //2, exit)
run = True
while run:
    
    if main_menu == True:
        SCREEN.blit(main_menuimage, (0,0))
        if exit_but.draw():
            run = False
        if start_but.draw():
            main_menu = False

    else:
        SCREEN.blit(scale, (0,0))
        level.create()
        player.update()
        if (player.rect.x > screen_width):
            draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            

    pygame.display.update()
import pygame
import  random
from sys import  exit

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0,255,0)

screen_width=900
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("snake game")
pygame.display.update()

exit_game=False
game_over = False
snake_x = 45
snake_y = 55
velocity_x=0
velocity_y=0

food_x=random.randint(20,screen_height/2)
food_y = random.randint(20,screen_width/2)
score=0
velocity_init=2
snake_size=20
fps = 120
clock= pygame.time.Clock()
font = pygame.font.SysFont(None,55)
snakea_size=10

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def plt_snake(gamewindow,color,snake_list,snake_size)   :
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

snake_list = []
snake_length = 1

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          exit_game=True
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=velocity_init
                velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x=-velocity_init
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-velocity_init
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=velocity_init
                velocity_x=0

    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score += 1

        food_x = random.randint(20, screen_height / 2)
        food_y = random.randint(20, screen_width / 2)
        snake_length +=5


    gamewindow.fill(green)
    text_screen("score  is = " + str(score * 10), red, 5, 5)
    pygame.draw.rect(gamewindow,red,[food_y,food_x,snakea_size,snakea_size])
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len (snake_list)>snake_length:
        del  snake_list[0]
    plt_snake(gamewindow,black,snake_list,snake_size)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
exit()


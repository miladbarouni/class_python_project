import pgzrun
import random
import os 

os.environ['SDL_VIDEO_CENTERED'] = '1'
TITLE = "Project"
WIDTH = 1000
HEIGHT = 700

street = Actor('busy_street_road' , (500,350 ))
car = Actor('car_up' , (565, 600))
car2 = Actor('left_car', (100, 400))
speed = 5

def update():
    global speed
    print(f'car pos : {car.pos} car angle : {car.angle}')
    
    if car.y <= -100 :
        car.y = 800
    if keyboard.up :
        car.y -= speed
    elif keyboard.down and car.y <= 625:
        car.y += speed
    car2.x += speed
    if car2.x >= 1200 :
        car2.x = -100 
    if car.colliderect(car2):
        speed = 0
    if keyboard.d :
        car2.flip_x  = True
def draw():
    street.draw()
    car.draw()
    car2.draw()

pgzrun.go()
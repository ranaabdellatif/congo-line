from dudraw import Color
from random import random
from random import randint
import dudraw
dudraw.set_canvas_size(500,500)

#creates dancer class
class Dancer:

    def __init__(self, x_pos, y_pos, x_target, y_target, radius, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_target = x_target
        self.y_target = y_target
        self.radius = radius
        self.color = color

    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_pos,self.y_pos,self.radius)

    def move(self):
        self.x_pos += (self.x_target - self.x_pos)*.1
        self.y_pos += (self.y_target - self.y_pos)*.1
    
    def set_target(self, x, y):
        self.x_target = x
        self.y_target = y

    def __str__(self)->str:
        return f'{self.x_pos} {self.x_target} {self.y_pos} {self.y_target}'

the_dancers = []

for i in range(10):
    the_dancers.append(Dancer(0.5,0.5,0.8,0.8,random()*0.05, Color(randint(0,255), randint(0,255), randint(0,255))))

key = ''
while key != 'q':
    #adds new dancer
    if key == 'n':
        the_dancers.append((Dancer(0.5,0.5,0.8,0.8,random()*0.05, Color(randint(0,255), randint(0,255), randint(0,255)))))
        key = ''

    dudraw.clear()

    the_dancers[0].set_target(dudraw.mouse_x(), dudraw.mouse_y())
    the_dancers[0].move()
    the_dancers[0].draw()
    for i in range(1, len(the_dancers)):
        the_dancers[i].set_target(the_dancers[i-1].x_pos, the_dancers[i-1].y_pos)
        the_dancers[i].move()
        the_dancers[i].draw()
    
    dudraw.show()
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()

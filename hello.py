from pico2d import *

open_canvas()

import os
os.getcwd()
os.chdir('C:/develop/Python/2DGP/2DGP_01/2d겜플')
os.listdir()

gra=load_image('grass.png')
ch=load_image('character.png')

x=0
while x < 800:
    clear_canvas_now()
    gra.draw_now(400,30)
    ch.draw_now(x,85)
    update_canvas()

    get_events()
    #for e in evts:
    # print(e)
    
    x +=2
    delay(0.02)


delay(1) #in seconds

close_canvas()

# turtle.onkey(some_function, 'w')
#turtle.onkey(other_function, 's')
#turtle.listen()





from pyglet.window import mouse
import pyglet
from pyglet.gl import *
from pyglet.window import key
import math

class Window():
    """Initialize the class window, with an array to save points, a default point size of 25, and a window"""

    def __init__(self, width, height):
        self.batch = pyglet.graphics.Batch()
        self.PointSize = 25
        self.window = pyglet.window.Window(
            width, height, resizable=True, vsync=True)
        self.button = False
        self.click_counter = 0
        self.L = []

    #First line drawer algorithm, slope intercept
    def slope_intercept(self, x1, y1, x2, y2):
        self.L.clear()
        dx = x2-x1 
        dy = y2-y1 
        x=x1
        y=y1
        m = dy/dx
       
        if dy>dx: 
            m=1/m
            b = x1-m*y1
        else:
            b = y1-m*x1

        if dx==0:
            for y in range(y1,y2+1):
                self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (x, y)))
                self.L.append([x,y])
        else:
            self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (x, y)))
            self.L.append([x,y])
            if dy>dx: 
                for y in range(y1,y2+1):
                    if dy != 0:
                        x = int(round(m*y+b))
                    self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (x, y)))
                    self.L.append([x,y])
            else:
                for x in range(x1,x2+1):
                    if dy != 0:
                        y = int(round(m*x+b))
                    self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (x, y)))
                    self.L.append([x,y])
    
    # Second Line drawer algorithm
    def digital_differential_analyzer(self, x1, y1, x2, y2):
        self.L.clear()
        dx = x2-x1 
        dy = y2-y1 
        M=max(abs(dx),abs(dy))
        dx_=dx/M
        dy_=dy/M
        x=x1+0.5
        y=y1+0.5
        i=0
        for i in range(0,M+1):
            self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (math.floor(x), math.floor(y))))
            self.L.append([x,y])
            x=x+dx_
            y=y+dy_
     
    # Third Line drawer algorithm
    def bresenham_line_algorithm(self, x1, y1, x2, y2):
        self.L.clear()

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        m = dy/float(dx)
        x, y = x1, y1   
        
        self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (x, y)))
        
        p = 2 * dy - dx
        
        if m > 1 :
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        
        

        
        self.L.append([x,y])

        for _ in range(2,dx):
            if p > 0 :
                y = y + 1 if y < y2 else y-1
                p = p + 2*(dy-dx)
            else:
                p = p + 2*dy
            
            x = x + 1 if x < x2 else x - 1

            self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (x, y)))
            self.L.append([x,y])
            
    #Function to set the point size
    def point_size(self, size):
        self.PointSize = size

    #Function to detect clicks with the mouse

    def action_mouse(self):
        pyglet.gl.glPointSize(self.PointSize)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.L:
                self.button = True
            else:
                self.button = False

        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            if button == mouse.LEFT:  # and self.button para la interfaz
                print('The left mouse button was pressed on. X: ', x, " Y: ", y)
                self.batch.add(1, pyglet.gl.GL_POINTS, None, ('v2i', (x, y)))
                self.click_counter += 1
                self.L.append([x, y]) 
                if self.click_counter == 2:
                    self.bresenham_line_algorithm(self.L[0][0],self.L[0][1],self.L[1][0],self.L[1][1])
                    print(self.L)
                    self.click_counter=0
                    self.L.clear()
            self.batch.draw()

window1=Window(300, 300)
window1.point_size(18)
window1.action_mouse()

pyglet.app.run()

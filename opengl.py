from pyglet.window import mouse
import pyglet
from pyglet.gl import *

class Window(): 
    """Initialize the class window, with an array to save points, a default point size of 25, and a window"""
    def __init__(self,width,height):
        self.batch = pyglet.graphics.Batch()
        self.PointSize=25
        self.window = pyglet.window.Window(width, height, resizable=True, vsync=True)
    
    "Function to set the point size"
    def point_size(self,size):
        self.PointSize = size

    
    "Function to detect clicks with the mouse"
    def action_mouse(self):
        pyglet.gl.glPointSize(self.PointSize)
        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()
        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
        
            if button == mouse.LEFT:
                print('The left mouse button was pressed on. X: ',x," Y: ",y)
                self.batch.add(1,pyglet.gl.GL_POINTS,None,('v2i', (x, y)))
            self.batch.draw()
    
window1 = Window(160,160)
window1.action_mouse()

pyglet.app.run()

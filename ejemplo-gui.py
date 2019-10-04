import pyglet
from pyglet_gui.theme import Theme
from pyglet_gui.buttons import Button
from pyglet_gui.manager import Manager


theme = Theme({"font": "Lucida Grande",
               "font_size": 12,
               "text_color": [0, 0, 0, 255],
               "gui_color": [255, 255, 255, 255],
               "button": {
                   "down": {
                       "image": {
                           "source": "down.png",
                           "frame": [8, 6, 2, 2],
                           "padding": [18, 18, 8, 6]
                       },
                       "text_color": [220, 220, 220, 255]
                   },
                   "up": {
                       "image": {
                           "source": "up.png",
                           "frame": [6, 5, 6, 3],
                           "padding": [18, 18, 8, 6]
                       },
                       "text_color": [0, 0, 0, 255]
                   }
               }
              }, resources_path='theme/')


# just to print something to the console, is optional.
def callback(is_pressed):
    print('Button was pressed to state', is_pressed)




window = pyglet.window.Window(640, 480, resizable=True, vsync=True)
batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    window.clear()
    batch.draw()

button = Button('Line', on_press=callback)
Manager(button, window=window, theme=theme, batch=batch)

pyglet.app.run()
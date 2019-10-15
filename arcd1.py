"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import os


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=1):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def click_area(self,x,y):
        
        if  x < self.center_x + self.width / 2 and x > self.center_x - self.width / 2 and \
            y < self.center_y + self.height / 2 and y > self.center_y - self.height / 2:
            
            return True
        return False    
        

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

def check_buttons_click_area(x,y,button_list):

    for button in button_list:
         if button.click_area(x,y):
            return True
    return False

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if button.click_area(x,y) and not button.pressed:
            button.on_press()
        elif button.click_area(x,y) and button.pressed:
            button.on_release()
        elif button.pressed and check_buttons_click_area(x,y,button_list):
            button.on_release()



def check_mouse_release_for_buttons(x, y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    
            

class Canvas(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)
        self.myButtons = None
        self.L=None
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.myButtons=[]
        self.L=[]
        self.L_aux=[]
        self.myButtons.append(TextButton(60, 570, 100, 40, "Slope", 14,"Arial"))
        self.myButtons.append(TextButton(60, 510, 100, 40, "D.D.A.", 14,"Arial"))
        self.myButtons.append(TextButton(60,450,100,40,"Bresenham",14))

    def on_draw(self):
        """
        Render the screen.
        """
        

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        for button in self.myButtons:
            button.draw()
        for point in self.L:
            arcade.draw_point(point[0],point[1], arcade.color.ZAFFRE, 10)
        

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        for point in self.L:
            arcade.draw_point(point[0],point[1], arcade.color.ZAFFRE, 10)
        

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass
    
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        
        Con self.L_aux len 1 puedes hacer que el segundo punto sea el de esta x e y
        """
        pass
    
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
        
        for _ in range(0,M+1):
            self.L.append([x,y])
            x=x+dx_
            y=y+dy_
        print(self.L)
        

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
       
        check_mouse_press_for_buttons(x, y, self.myButtons)
        if check_buttons_click_area(x, y, self.myButtons) == False:     
            for button in self.myButtons:
                if button.pressed:
                    self.L_aux.append([x,y])
                    if len(self.L_aux) == 2:
                        if button.text == 'Slope':
                            print("Slope")       
                        elif button.text == 'D.D.A.':
                            self.digital_differential_analyzer(self.L_aux[0][0],self.L_aux[0][1],self.L_aux[1][0],self.L_aux[1][1])
                        elif button.text == 'Bresenham':
                            print ("Bresenham")
                        self.L_aux.clear()

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        check_mouse_release_for_buttons(x, y, self.myButtons)

    

def main():
    """ Main method """
    canvas = Canvas(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    canvas.setup()
    arcade.run()


if __name__ == "__main__":
    main()
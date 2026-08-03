"""
The main menu class used to create the main menu, pause menu, and death menu
of the dungeon game.
"""
from ursina import Entity, Text, ButtonList, Func, application, Ursina, camera

app = Ursina()
BACKGROUND = Entity(model='quad', texture='Assets/menu background.jpg', z=1,
                    scale=(1.8,1))

class MainMenu(Entity):
    def __init__(self, start_func, resume_func, bg=BACKGROUND,
                 header='The Dungeon', text='Start', y=0, enabled=True):
        super().__init__(parent=camera.ui, ignore_paused=True,
                         enabled=enabled)

        self.main_menu = Entity(parent=self, enabled=True, ignore_paused=True)
        self.started = False
        
        self.background = bg
        self.background.parent=self.main_menu
        self.background.enabled = True

        self.start_function = start_func

        Text(header, parent=self.main_menu, y=0.25, x=0, z=-10, scale=5,
             origin=(0,0))

        # Initialize the buttons for the main menu
        self.start_buttons = ButtonList(button_dict={
            text: Func(self.start_function),
            "Exit": Func(lambda: application.quit())},
            y=y, z=-10, parent=self.main_menu, ignore_paused=True)

        # Initialize the buttons for the pause menu
        self.pause_buttons = ButtonList(button_dict={
            "Resume": Func(resume_func),
            "Exit": Func(lambda: application.quit())
        },y=y, z=-10, parent=self.main_menu, enabled=False, ignore_paused=True)

# Debug the main menu
if __name__ == '__main__':
     app = Ursina()
     MainMenu('q', '1')
     app.run()
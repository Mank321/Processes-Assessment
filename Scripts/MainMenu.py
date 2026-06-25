from ursina import Entity, Text, camera, Sprite, color, ButtonList, Func, application, Button, Ursina

class MainMenu(Entity):
    def __init__(self, start_func, resume_func):
        super().__init__(parent=camera.ui, ignore_paused=True)

        self.main_menu = Entity(parent=self, enabled=True)
        self.started = False

        self.background = Entity(model='quad', texture='Assets/menu background.jpg', parent=self.main_menu, z=1, scale=(1.8,1))

        Text("MAIN MENU", parent=self.main_menu, y=0.4, x=0, z=-10, origin=(0,0))

        self.start_buttons = ButtonList(button_dict={
            "Start": Func(start_func),
            "Exit": Func(lambda: application.quit())
        },y=0, z=-10,parent=self.main_menu)

        self.pause_buttons = ButtonList(button_dict={
            "Resume": Func(resume_func),
            "Exit": Func(lambda: application.quit())
        },y=0, z=-10, parent=self.main_menu, enabled=False)
    
    def switch(self, new_menu, old_menu):
        new_menu.enable()
        old_menu.disable()

    def input(self, key):
        if self.main_menu.enabled and key == "escape":
            application.quit()

if __name__ == '__main__':
     app = Ursina()
     MainMenu('q', '1')
     app.run()
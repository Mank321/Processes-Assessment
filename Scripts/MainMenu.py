from ursina import Entity, Text, ButtonList, Func, application, Ursina, camera

app = Ursina()
ORIGIN_BACKGROUND = Entity(model='quad', texture='Assets/menu background.jpg', z=1, scale=(1.8,1))

class MainMenu(Entity):
    def __init__(self, start_func, resume_func, bg=ORIGIN_BACKGROUND, header='Main Menu', text='Start', y=0, enabled=True):
        super().__init__(parent=camera.ui, ignore_paused=True, enabled=enabled)

        self.main_menu = Entity(parent=self, enabled=True, ignore_paused=True)
        self.started = False

        self.background = bg
        self.background.parent=self.main_menu
        self.background.enabled = True

        self.start_function = start_func

        Text(header, parent=self.main_menu, y=0.4, x=0, z=-10, size=50, origin=(0,0))

        self.start_buttons = ButtonList(button_dict={
            text: Func(self.execute_start),
            "Exit": Func(lambda: application.quit())
        },y=y, z=-10,parent=self.main_menu, ignore_paused=True)

        self.pause_buttons = ButtonList(button_dict={
            "Resume": Func(resume_func),
            "Exit": Func(lambda: application.quit())
        },y=y, z=-10, parent=self.main_menu, enabled=False, ignore_paused=True)
    
    def execute_start(self):
        if self.start_function:
            self.start_function()

    def input(self, key):
        if self.main_menu.enabled and key == "escape":
            application.quit()

if __name__ == '__main__':
     app = Ursina()
     MainMenu('q', '1')
     app.run()
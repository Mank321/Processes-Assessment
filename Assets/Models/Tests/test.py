from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class MountainWorld(Entity):
    def __init__(self):
        super().__init__()        
        
        self.mountain_collider = Entity(
            parent=self,
            model='collider.obj',
            scale=(1, 1, 1),
            texture='ground.png',
            position=(0, -1, 0),
            rotation_y=45,
            double_sided=True,
            collider='mesh',
            visible=False)
        self.mountain = Entity(
            parent=self,
            model='ground.obj',
            scale=(1, 1, 1),
            texture='ground.png',
            position=(0, -1, 0),
            rotation_y=45,
            double_sided=True)
        self.floor = Entity(
            parent=self,
            model='floor.obj',
            scale=(1,1,1),
            color=color.red,
            position=(0,0,0),
            rotation=0,
            double_sided=True,
            collider='mesh')

app = Ursina()

world = MountainWorld()
player = FirstPersonController()
#EditorCamera()

app.run()
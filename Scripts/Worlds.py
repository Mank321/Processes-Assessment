from ursina import Entity, Text, color, Vec3
from ursina.shaders import unlit_shader
from Scripts.Objects import Stall, Tree, Gate, Sign
from Scripts.Monster import Monster
from Scripts.MonsterStats import CENTAUR_STATS

class TutorialWorld(Entity):
    def __init__(self, manager):
        super().__init__()
        self.manager  = manager
        self.ground = Entity(parent=self, model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))

        self.wall = Entity(parent=self, model='Assets/Models/Wall/Wall.obj', texture='Assets/Models/Wall/texture.png',
                           double_sided=True, scale=(0.5,1,0.5), collider='mesh', position=(0,5,15))
        
        self.next_gate = Gate(self.manager, parent=self, position=(0,-0.7,30), locations='tutorial.market')

        self.desc1 = '             Welcome to the dungeon!\n\nUse the mouse to move around\nPress "W" to move forward, "S" to move backward\nPress "A" to move right and "D" to move left\nPress the spacebar to jump'
        self.text1 = Text(parent=self, text=self.desc1, position=(-8,5,9), scale=30, color=color.white)
        
        self.desc2 = 'Attack the monster up ahead by left clicking!\n                     Try not to get hit!'
        self.text2 = Text(parent=self, text=self.desc2, position=(-8,4,19), scale=30, color=color.white)

        self.monster = Monster(self.manager, parent=self, monster_stats=CENTAUR_STATS, is_tutorial=True, gate=self.next_gate, position=Vec3(0,0,25), rotation=Vec3(0,180,0))

        self.colliders = []
        self.map = ['        TTTTTTTT        ',
                    '       TTTT  TTTT       ',
                    '      TTTT    TTTT      ',
                    '      TT        TT      ',
                    '      TT        TT      ',
                    '      TT        TT      ',
                    '      TT        TT      ',
                    '      TT        TT      ',
                    '      TT        TT      ',
                    '      TTT      TTT      ',
                    '       TTT    TTT       ',
                    '        TTTTTTTT        ']
        self.map.reverse()
        for z, row in enumerate(self.map):
            for x, col in enumerate(row):
                if col == 'T':
                    Tree(manager, ((x*4)-45, 0, (z*4)-7),parent=self)

        manager.incomplete_gates.append(self.next_gate)
        
    def update(self):
        if self.manager.player.y <= -20:
            self.manager.player.position=(0,1,0)


class MarketWorld(Entity):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.ground = Entity(parent=self,model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))
        
        self.wall = Entity(parent=self,model='Assets/Models/Wall/Wall.obj', texture='Assets/Models/Wall/texture.png',
                    double_sided=True,scale=(0.2,1,0.5), collider='mesh', position=(0,5,0))

        self.return_gate = Gate(self.manager, parent=self, position=(0,-0.7,-5), locations='market.tutorial', complete=True, rotation_y=180)
        self.next_gate = Gate(self.manager, parent=self, position=(0,-0.7,20), locations='market.centaur', complete=True)

        self.stall = Stall(self.manager,parent=self, position=(5,0,5), name='Market')
        self.emergency_sign = Sign(parent=self, position=(0,1,40), text=f'Press L!', rotation_y=90)

        self.colliders = [self.stall.collision_box]

    def update(self):
        if self.manager.player.y <= -20:
            self.manager.player.position=(0,1,0)

class RebirthWorld(Entity):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

        self.temple = Entity(parent=self, model='Assets/Models/Temple/templeV3.obj', texture='Assets/Models/Temple/texture.png',
                             double_sided=True, scale=(0.4,0.78,0.4), position=(0,-6.5,50), collider='mesh', rotation_y=-90)
        self.cloud = Entity(parent=self, model='Assets/Models/Temple/cloud.obj', texture='Assets/Models/Temple/cloudtexture.png', double_sided=True,
                            scale=(40,20,40), position=(70,-20,0), shader=unlit_shader)

        self.statue = Entity(parent=self.temple, model='Assets/Models/Temple/zeusStatue.obj', texture='Assets/Models/Temple/zeusTexture.png',
                             double_sided=True, scale=(0.6,0.6,0.6), position=(17,8,0), collider='box', rotation_y=90)
        self.stall = Stall(self.manager, parent=self.temple, position=(17,10,15), scale=(0.25,0.35,0.25), name='Rebirth')

        self.cloud_box = Entity(parent=self, model='cube', color=color.white, wireframe=True, visible=self.manager.debug_mode,
                                collider='box', scale=(120,50,120), position=(0,25,50))
        self.return_gate = Gate(self.manager, parent=self, position=(0,-0.7,-5), locations='rebirth.chimera', complete=True, rotation_y=180)

        self.sky = Entity(parent=self, model='Assets/Models/Temple/sky.fbx', texture='Assets/Models/Temple/night.jpg',
                          double_sided=True, scale=0.8, position=(0,0,0), rotation_z=180)
        self.colliders = [self.stall.collision_box]

    def update(self):
        if self.manager.player.y <= -40:
            self.manager.player.position=(0,1,0)
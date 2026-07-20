from ursina import Entity, Text, color, Vec3
from Scripts.Objects import Stall, Tree, Gate
from Scripts.Monster import Monster
from Scripts.MonsterStats import CENTAUR_STATS

class TutorialWorld(Entity):
    def __init__(self, manager):
        super().__init__()
        self.ground = Entity(parent=self,model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))

        self.wall = Entity(parent=self,model='Assets/Models/Wall/Wall.obj', texture='Assets/Models/Wall/texture.png',
                    double_sided=True,scale=(0.005,0.01,0.005), collider='mesh', position=(0,5,10))
        
        self.gate = Gate(manager, parent=self, position=(0,-0.7,30), locations='tutorial.market')

        self.desc1 = '             Welcome to the dungeon!\n\nUse the mouse to move around\nPress "W" to move forward, "S" to move backward\nPress "A" to move right and "D" to move left\nPress the spacebar to jump'
        self.text1 = Text(parent=self, text=self.desc1, position=(-8,5,9), scale=30, color=color.white)
        
        self.desc2 = 'Attack the monster up ahead by left clicking!\n                     Try not to get hit!'
        self.text2 = Text(parent=self, text=self.desc2, position=(-8,4,19), scale=30, color=color.white)

        self.monster = Monster(manager, parent=self, monster_stats=CENTAUR_STATS, is_tutorial=True, gate=self.gate, position=Vec3(0,0,25), rotation=Vec3(0,180,0))

        self.colliders = [self.gate.collision_box]
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


class MarketWorld(Entity):
    def __init__(self, manager):
        super().__init__()
        self.ground = Entity(parent=self,model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))
        
        self.wall = Entity(parent=self,model='Assets/Models/Wall/Wall.obj', texture='Assets/Models/Wall/texture.png',
                    double_sided=True,scale=(0.2,1,0.5), collider='mesh', position=(0,5,0))

        self.tutorial_gate = Gate(manager, parent=self, position=(0,-0.7,-5), locations='market.tutorial', complete=True, rotation_y=180)
        self.centaur_gate = Gate(manager, parent=self, position=(0,-0.7,20), locations='market.centaur', complete=True)

        self.stall = Stall(manager,parent=self, position=(5,0,5), rotation_y=-90)

        self.colliders = [self.tutorial_gate.collision_box, self.stall.collision_box, self.centaur_gate.collision_box]
from ursina import Entity
from Scripts.Objects import Tree

class CentaurMap(Entity):
    def __init__(self, manager, parent):
        super().__init__(parent=parent, model='Assets/Models/Centaur/World/ground.fbx', texture='Assets/Models/Centaur/World/ground.png',
                         double_sided=True, scale=(.05,.05,.05), position=(5,0,80), rotation_y=90)
        
        self.manager = manager
        self.ground_collider = Entity(model='cube', parent=self, collider='box', position=(0,0,0), scale=(5000,1,5000),
                                      visible=manager.debug_mode, wireframe=True)
        self.left_collider = Entity(model='cube', parent=self, collider='box', position=(0,0,-1500), scale=(5,500,5000), rotation=(0,85,0),
                                      visible=manager.debug_mode, wireframe=True)
        self.right_collider = Entity(model='cube', parent=self, collider='box', position=(0,0,1600), scale=(5,500,5000), rotation=(0,85,0),
                                      visible=manager.debug_mode, wireframe=True)
        self.front_collider = Entity(model='cube', parent=self, collider='box', position=(-1700,0,0), scale=(5,500,5000), rotation=(0,5,0),
                                      visible=manager.debug_mode, wireframe=True)
        self.back_collider = Entity(model='cube', parent=self, collider='box', position=(1800,0,0), scale=(5,500,5000), rotation=(0,-5,0),
                                      visible=manager.debug_mode, wireframe=True)
        self.front_left_collider = Entity(model='cube', parent=self, collider='box', position=(-1500,0,450), scale=(400,500,2000), rotation=(0,-80,0),
                                      visible=manager.debug_mode, wireframe=True)
        self.front_left_collider2 = Entity(model='cube', parent=self, collider='box', position=(-1500,0,700), scale=(300,500,800), rotation=(0,-40,0),
                                      visible=manager.debug_mode, wireframe=True)
        self.front_right_collider = Entity(model='cube', parent=self, collider='box', position=(-1350,0,-750), scale=(350,500,2000), rotation=(0,70,0),
                                      visible=manager.debug_mode, wireframe=True)
        self.map = ['TTTWWTTTTTTWWWWW',
                    '  TWWWTO TWWWWT ',
                    ' M TWW B WWWTT  T',
                    'TM TWWW  WWTT     ',
                    '   TWWWM WWT  MM  T',
                    'T   TWW MWWT       ',
                    '    TWW  WWT  T   T',
                    '  M  TTMMTT        ',
                    'T     M  M        T',
                    '    T   M    T MM  T',
                    'T         MM        ',
                    'T   MM T      T  M  ',
                    '    M     M       T',
                    'T           T  M  T',
                    'MM  T   MM         ',
                    'WT  MM        T   T',
                    'W   M    T  M    T ',
                    'WW   T      M    ',
                    'WWWT    S     TT',
                    'WWWWMM  I  T T',
                    'WWWWW TT T']
        for x, row in enumerate(self.map):
            for z, col in enumerate(row):
                if col == 'T':
                    Tree(manager, ((x*200)-1700, 0, (z*200)-1600), parent=self, scale=20)
        
        self.out_position = 0

        self.grass = Entity(parent=self, model='Assets/Models/Centaur/World/grass.fbx', texture='Assets/Models/Centaur/World/Grass_gradient.png',
                            double_sided=True)

    def update(self):
        if self.manager.player.y <= -21:
            self.manager.player.position=(0,0,0)


class BasiliskMap(Entity):
    def __init__(self, manager, parent):
        super().__init__(parent=parent, rotation_y=90, position=(-2,7,-7), scale=(0.5,1,0.5))
        self.hallway = Entity(parent=self, model='Assets/Models/Basilisk/World/hall.obj', texture='Assets/Models/Basilisk/World/Hall.png',
                               double_sided=True, collider='mesh')
        self.head = Entity(parent=self, model='Assets/Models/Basilisk/World/head.obj', texture='Assets/Models/Basilisk/World/Head.png',
                            double_sided=True, collider='mesh')
        self.main_room = Entity(parent=self, model='Assets/Models/Basilisk/World/main.obj', texture='Assets/Models/Basilisk/World/Main_Room.png',
                                 double_sided=True, collider='mesh')
        self.floor = Entity(parent=self, model='Assets/Models/Basilisk/World/floor.obj', texture='Assets/Models/Basilisk/World/Floor.png',
                             double_sided=True, collider='mesh')
        self.water = Entity(parent=self, model='Assets/Models/Basilisk/World/water.fbx', texture='Assets/Models/Basilisk/World/Water.png',
                             double_sided=True, scale=0.01, rotation_y=180, z=6)
        self.snakes = Entity(parent=self, model='Assets/Models/Basilisk/World/snakes.fbx', texture='Assets/Models/Basilisk/World/Snake.png',
                              double_sided=True, scale=0.01, rotation_y=180, z=6)
        self.snake_collider1 = Entity(parent=self, model='cube', collider='box', position=(-77.5,-3,-10), scale=(75,10,10),
                                      visible=manager.debug_mode, wireframe=True)
        self.snake_collider2 = Entity(parent=self, model='cube', collider='box', position=(-77.5,-3,17), scale=(75,10,10),
                                      visible=manager.debug_mode, wireframe=True)
        self.map = ['                 O                     ',
                    '                                       ',
                    '                                       ',
                    '                                       ',
                    '  TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT  ',
                    ' T                                   T ',
                    ' T                 B                 T ',
                    'T        M                      M     T',
                    'T                                     T',
                    'T                                     T',
                    'T                     M               T',
                    'T    M                                T',
                    'T                                M    T',
                    'T           M                         T',
                    'T                                     T',
                    'T                   M                 T',
                    'T                             M       T',
                    'T                                     T',
                    'T        M                            T',
                    'T                                     T',
                    ' T                 M                  T',
                    ' T                              M     T',
                    '  T    M                              T',
                    '  T                     M            T ',
                    '   T                                T  ',
                    '    T       M                      T   ',
                    '     T                      M     T    ',
                    '      T                          T     ',
                    '        T                      T       ',
                    '         T       M            T        ',
                    '           T            M   T          ',
                    '             T            T            ',
                    '              T          T             ',
                    '              T          T             ',
                    '              T  M       T             ',
                    '              T          T             ',
                    '              T          T             ',
                    '              T         MT             ',
                    '              T          T             ',
                    '              TTTTT  TTTTT             ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T MT                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  TM T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T MT                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  TM T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '                  T  T                 ',
                    '             TTTTTT  TTTTTT            ',
                    '                                       ',
                    '                  S                    ',
                    '                                       ',
                    '                                       ',
                    '                  I                    ',]
        
        self.out_position = 3
        self.manager = manager

    def update(self):
        if self.manager.player.y <= -21:
            self.manager.player.position=(0,0,0)


class GorgonMap(Entity):
    def __init__(self, manager, parent):
        super().__init__(parent=parent, model='Assets/Models/Gorgon/World/world.obj', texture='Assets/Models/Gorgon/World/texture.png', double_sided=True,
                         position=(0,2,0), scale=(1,1.2,1), rotation_y=180, collider='mesh')
        self.statues = Entity(parent=self, model='Assets/Models/Gorgon/World/gorgon_statues.fbx', texture='Assets/Models/Gorgon/World/Statues/texture.png', double_sided=True,
                              scale=(0.01,0.01,0.01))
        self.positions = [(-10, -0.5, 20), (-23.8, -0.5, 14.71), (-24.7, -0.5, 32.7), (-14.282, -0.5, 33.2),(-43.2, -0.5, 35.6),(-45.3, -0.5, 19.9), (-23.5, -0.5, 56.9),
                          (-47.3, -0.5, 45.6),(-62.9, -0.5, 40.6),(-73.5, -0.5, 56.9),(-38.6, -0.5, 77.9),(-46.4, -0.5, 81.3),(-69.8, -0.5, 71.8),(-24.7, -0.5, 95.1),
                          (1.5, -0.5, 81.4),(23.2, -0.5, 82.6),(15.2, -0.5, 92.8),(-30, -0.5, 106.7),(-22, -0.5, 115.8),(-41.3, -0.5, 116.7),(-42.6, -0.5, 139.7),
                          (-45.5, -0.5, 169.8),(-51.2, -0.5, 209,),(-57.3, -0.5, 180.2),(-45.3, -0.5, 183.3),(-28.2, -0.5, 194.1),(-39.5, -0.5, 204.6),(-28, -0.5, 208),
                          (-12.1, -0.5, 212.3),(-16.7, -0.5, 217.5),(24.3, -0.5, 105.3),(38.2, -0.5, 100.3),(53.2, -0.5, 94.4),(57, -0.5, 116.5),(72, -0.5, 119.1),
                          (67.4, -0.5, 141.8),(86.2, -0.5, 156.7),(63.6, -0.5, 156.5),(79.8, -0.5, 164.3),(59.6, -0.5, 170.2),(82.8, -0.5, 178.3),(49.6, -0.5, 174.8),
                          (93.6, -0.5, 173.1),(53.8, -0.5, 194.2),(93.5, -0.5, 194),(53.57, -0.5, 202.4),(-10.5, -0.5, 226.5),(35.8, -0.5, 196.4),(23.8, -0.5, 204.6),
                          (5.1, -0.5, 204),(77.3, -0.5, 200.3),(76.3, -0.5, 216.5),(66, -0.5, 219.1),(52.7, -0.5, 218.8),(53.6, -0.5, 235),(71.3, -0.5, 240.1),
                          (70, -0.5, 233),(60.4, -0.5, 259.9),(48.8, -0.5, 249.7),(41.8, -0.5, 263),(39.4, -0.5, 275.8),(24.2, -0.5, 265.3),(25.9, -0.5, 278),
                          (17, -0.5, 279.8),(12, -0.5, 261),(1.9, -0.5, 252.6),(-6.5, -0.5, 236.5),(-10.8, -0.5, 239.4),(-19.4, -0.5, 251.2),(-1.7, -0.5, 264.2),
                          (-0.6, -0.5, 279.3),(12.2, -0.5, 288.7),(-15.1, -0.5, 288.8),(-25.1, -0.5, 268.8),(-21.5, -0.5, 283.2),(-29.3, -0.5, 296),(-24.4, -0.5, 300.4),
                          (-30, -0.5, 314.7),(-47.6, -0.5, 294.6),(-56.8, -0.5, 296.2),(-65.2, -0.5, 200.5),(-78.3, -0.5, 204.9),(-73.5, -0.5, 219),(-57.7, -0.5, -0.5, 223.3),
                          (-68.1, -0.5, 237.7),(-56.9, -0.5, 249.6),(-64, -0.5, 264.7),(-62, -0.5, 307),(-43.5, -0.5, 315.3),(-50, -0.5, 331.5),(-60, -0.5, 322.5),
                          (-71, -0.5, 333.3),(-57, -0.5, 342.5),(-83.1, -0.5, 343.8),(-92.1, -0.5, 334.9),(-47.2, -0.5, 358.2),(-78, -0.5, 361.8),(-92.3, -0.5, 375.5),
                          (-59.8, -0.5, 373.4),(-46.4, -0.5, 389),(-30.3, -0.5, 373.4),(-81.2, -0.5, 390.9),(-72.4, -0.5, 406.2),(-102.8, -0.5, 392.1),(-110, -0.5, 412.9),
                          (-85.2, -0.5, 413),(-65.4, -0.5, 422.8),(-41.5, -0.5, 442.8),(-68.2, -0.5, 439.8),(-90.1, -0.5, 433.6), (-123.8, -0.5, 435.1),(-104, -0.5, 436.4)]
        self.next_gate_position = (-87,4,514)
        self.boss_position = (-87,5,510)
        self.manager = manager

    def update(self):
        if self.manager.player.y <= -21:
            self.manager.player.position=(0,0,0)


class ChimeraMap(Entity):
    def __init__(self, manager, parent):
        super().__init__(parent=parent, model='Assets/Models/Chimera/World/world_V3.obj', texture='Assets/Models/Chimera/World/texture.png',
                         double_sided=True, collider='mesh', position=(0,0,0), scale=(1,2,1))
        
        self.positions = [(5.2,-1,-18.4),(-23.9,-1.5,14.7),(13.7,-5,18.8),(-52.1,5,9.7),(-54,6,-6.1),(-78.5,0.5,25.2),(-59.4,2,-34.3),(-107.3,-0.5,20.7),
                          (-24.1,17.2,-74.6),(10.6,11.6,-90.8),(25.1,2,-121.8),(26,10.2,-111.1),(-133.2,-6.7,-3),(-172.7,-7.9,-6.8),(-190,-8.2,-34.6),(-128.5,-9.3,-54.2),
                          (-112.3,-7.8,-118.5),(-138,-7.5,-146.4),(-34.6,6.3,94.9),(-86.4,2.6,126),(-82.9,51,192.2),(-49.4,17.4,169.5),(42.4,-7.8,98.4),(80.1,2.3,83.4),
                          (175.2,-4.1,189.5),(124.6,-0.8,24.1),(27.9,-0.2,136.3),(67.7,-0.8,165.1),(143.6,-3.7,170.4),(209,-0.1,115.1)]

        self.next_gate_position = (215.3,-4.8,171.3)
        self.boss_position = (205,-2.6,162.4)
        self.manager = manager

    def update(self):
        if self.manager.player.y <= -21 and not self.manager.player.lava_protection:
            self.manager.player.health -= 10
        if self.manager.player.y <= -50:
            self.manager.player.position=(0,0,0)

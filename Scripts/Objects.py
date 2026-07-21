from ursina import Entity, Text, time, color, scene

class Tree(Entity):
    def __init__(self, manager, position, parent, scale=1):
        super().__init__(model='Assets/Models/Tree/treev2.fbx',
                         texture='Assets/Models/Tree/texture.png',
                         scale=(0.05,0.04,0.05)*scale, position=position,
                         double_sided=True, name='tree', parent=parent)

        self.collision_box = Entity(model='cube', parent=self,
                                    position=(0,125,0), scale=(70,250,70),
                                    collider='box', visible=manager.debug_mode,
                                    wireframe=True)

class Sign(Entity):
    def __init__(self, parent, position, text, rotation_y=90):
        super().__init__(parent=parent, model='Assets/Models/Sign/signV2.fbx', texture='Assets/Models/Sign/sign texture.jpg',
                         double_sided=True, scale=(.001,.002,.001), position=position, rotation_y=rotation_y)
        self.text = Text(parent=self, text=text, scale=13000, 
                         position=(300,800,-600),
                         color=color.white, rotation_y=-90)

class Stall(Entity):
    def __init__(self, manager, parent, position, rotation_y):
        super().__init__(parent=parent,model='Assets/Models/Stall/Stall/stall1.fbx', texture='Assets/Models/Stall/Stall/stall_texture.png',
                         double_sided=True, scale=(0.1,0.25,0.1), position=position, rotation_y=rotation_y)

        self.props = Entity(model='Assets/Models/Stall/Props/props.fbx', texture='Assets/Models/Stall/Props/props_texture.png',
                            parent=self, double_sided=True,scale=(1,1,1), position=(0,0,0))

        self.collision_box = Entity(model='cube', parent=self, name='Stall',
                                    position=(0,0,0), scale=(40,50,40),
                                    collider='box', visible=manager.debug_mode,
                                    wireframe=True)
        self.merchant = Entity(model='Assets/Models/Stall/Merchant/merchant.fbx', texture='Assets/Models/Stall/Merchant/texture.jpg',
                               double_sided=True, parent=self, scale=(.11,.11,.11), position=(0,0,0))


class Gate(Entity):
    def __init__(self, manager, position, locations, parent, complete=False, scale=(0.002,0.004,0.002), rotation_y=0):
        super().__init__(parent=parent, complete=complete, position=(0,-1,0))

        self.complete = complete
        self.name = f'gate.{locations}.incomplete' if not self.complete else f'gate.{locations}.complete'
        self.to_where = locations.split('.')[1]
        
        # Sign
        self.sign = Sign(self, position=(position[0]+3, position[1]+3, position[2]), text=self.to_where.title(), rotation_y=rotation_y+90)

        # Vertex
        self.anchor = Entity(parent=parent, model='cube', scale=(0.5,1,0.5), position=position, y=position[1]-1)
        self.portal = Entity(parent=self.anchor, model='Assets/Models/Gate/Sections/new.fbx', texture='Assets/Models/Gate/Textures/vertex',
                scale=0.045, rotation_y=rotation_y+90, double_sided=True)
        self.portal.y += 6.5
        self.portal.alpha = 1 if self.complete else 0

        # Other parts
        self.frame = Entity(parent=parent, model='Assets/Models/Gate/Sections/frame.fbx',
                            texture='Assets/Models/Gate/Textures/frame.png',
                            double_sided=True, scale=scale, rotation_y=rotation_y-90, position=position)
        self.base = Entity(parent=parent, model='Assets/Models/Gate/Sections/base.fbx',
                           texture='Assets/Models/Gate/Textures/stone.png', double_sided=True,
                           scale=scale, rotation_y=rotation_y-90, position=position)
        self.crystals = Entity(parent=parent, model='Assets/Models/Gate/Sections/crystals.fbx',
                               texture='Assets/Models/Gate/Textures/Gem.png', double_sided=True,
                               scale=scale, rotation_y=rotation_y-90, position=position)
        self.pattern = Entity(parent=parent, model='Assets/Models/Gate/Sections/pattern.fbx',
                              double_sided=True,scale=scale, rotation_y=rotation_y+90, position=position, z=position[2]-0.33)
        self.pattern.color = color.green if self.complete else color.red
        self.pattern.z = position[2]-0.33 if rotation_y == 0 else position[2]+0.33

        self.collision_box = Entity(parent=parent, model='cube', name=self.name, rotation_y=rotation_y, position=position, scale=(4,11,1),
                                    origin=(0,-.5,0), collider='box', visible=manager.debug_mode, wireframe=True)

    def update(self):
        self.portal.rotation_x += 50 * time.dt
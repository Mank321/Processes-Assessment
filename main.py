from ursina import *
from Scripts.HealthBar import HealthBar
from Scripts.MainMenu import MainMenu
from ursina.shaders import unlit_shader


CENTAUR_STATS = {'name': 'Centaur',
                 'health': 10,
                 'damage': 1,
                 'worth':1,
                 'speed':100,
                 'sight':10,
                 'closeness':2,
                 'attack_speed': 1,
                 'scale': Vec3(0.02,0.024,0.015),
                 'collider_scale': Vec3(100,250,170),
                 'collider_position': Vec3(0,125,0),
                 'boss_scale':Vec3(2,3,2),
                 'boss_collider_scale':Vec3(0.7,3,1.5),
                 'boss_collider_pos': Vec3(0,1,0),
                 'boss_rotation': 0,
                 'boss_speed':1.5,
                 'boss_sight':15,
                 'boss_closeness':2}

BASILISK_STATS = {'name': 'Basilisk',
                'health': 100,
                'damage': 10,
                'worth':10,
                'speed':35000,
                'sight':15,
                'closeness': 5.5,
                'attack_speed': 1,
                'scale': Vec3(0.0001,0.0002,0.0001),
                'collider_scale': Vec3(10000,40000,100000),
                'collider_position': Vec3(1,20000,1),
                'boss_scale':Vec3(2,6,2),
                'boss_collider_scale': Vec3(6,3,3),
                'boss_collider_pos': Vec3(-1,0,0),
                'boss_rotation': 90,
                'boss_speed':3,
                'boss_sight':20,
                'boss_closeness':10}

GORGON_STATS = {'name': 'Gorgon',
                'health': 1000,
                'damage': 100,
                'worth':20,
                'speed':300,
                'sight':12,
                'closeness':2.5,
                'attack_speed': 1,
                'scale': Vec3(0.005,0.01,0.005),
                'collider_scale': Vec3(200,800,150),
                'collider_position': Vec3(100,400,0),
                'boss_scale':0.05,
                'boss_collider_scale':Vec3(100,200,100),
                'boss_collider_pos': Vec3(0,100,0),
                'boss_rotation': 0,
                'boss_speed':50,
                'boss_sight':20,
                'boss_closeness':3}

CHIMERA_STATS = {'name': 'Chimera',
                'health': 1000,
                'damage': 100,
                'worth':20,
                'speed':300,
                'sight':12,
                'closeness':2.5,
                'attack_speed': 1,
                'scale': Vec3(0.005,0.01,0.005),
                'collider_scale': Vec3(200,800,150),
                'collider_position': Vec3(100,400,0),
                'boss_scale':0.05,
                'boss_collider_scale':Vec3(100,200,100),
                'boss_collider_pos': Vec3(0,100,0),
                'boss_rotation': 0,
                'boss_speed':50,
                'boss_sight':20,
                'boss_closeness':3}


class GameManager(Entity):
    """."""
    def __init__(self):
        """."""
        super().__init__()
        self.player = None
        self.ui_state = None 
        self.tutorial_world = None
        self.market_world = None
        self.centaur_world = None
        self.basilisk_world = None
        self.gorgon_world = None
        self.chimera_world = None

        self.locations = [
            'Tutorial',
            'Market',
            'Centaur',
            'Basilisk',
            'Gorgon',
            'Chimera',
            'Hydra',
        ]

        self.location = None
        self.debug_mode = False

    def start_game(self):
        """."""
        main_menu.started = True
        main_menu.enabled = False
        main_menu.background.enabled = False
        
        # Initialize the main classes
        self.ui_state = UIState(None)
        self.player = Player(self.ui_state, self)
        self.ui_state.player = self.player         

        # Load the tutorial world at the beginning 
        self.tutorial_world = TutorialWorld(self)

        self.location = 'tutorial'
        self.sky = Sky()


    def pause_game(self):
        mouse.locked = False
        self.ui_state.teleport_hud.enabled = False
        main_menu.start_buttons.enabled = False
        main_menu.pause_buttons.enabled = True
        main_menu.background.enabled = True
        main_menu.enabled = True
        main_menu.background.z = -1
        application.paused = True

    def resume_game(self):
        main_menu.enabled = False
        main_menu.background.enabled = False
        mouse.locked = True
        main_menu.background.z = 1
        application.paused = False
    
    def switch_scenes(self, gate):
        """."""
        self.player.position = (0,1,0)
        new_scene_name = gate.split('.')[1]
        old_scene_name = gate.split('.')[0]

        self.location = new_scene_name
        
        self.scenes = {'tutorial': self.tutorial_world, 'market': self.market_world,
                       'centaur': self.centaur_world, 'basilisk': self.basilisk_world,
                       'gorgon': self.gorgon_world, 'chimera': self.chimera_world}
        
        new_scene = self.scenes[new_scene_name]
        old_scene = self.scenes[old_scene_name]

        if new_scene == None:
            if new_scene_name == 'market':
                self.market_world = MarketWorld(self)
                new_scene = self.market_world
                self.ui_state.teleport_buttons['Market'].on_click = lambda: self.player.teleport('market')
                self.ui_state.teleport_buttons['Market'].disabled = False
            elif new_scene_name == 'centaur':
                self.centaur_world = LevelCreator(self, monster_stats=CENTAUR_STATS)
                new_scene = self.centaur_world
                self.ui_state.teleport_buttons['Centaur'].on_click = lambda: self.player.teleport('centaur')
                self.ui_state.teleport_buttons['Centaur'].disabled = False
            elif new_scene_name == 'basilisk':
                self.basilisk_world = LevelCreator(self, monster_stats=BASILISK_STATS)
                new_scene = self.basilisk_world
                self.ui_state.teleport_buttons['Basilisk'].on_click = lambda: self.player.teleport('basilisk')
                self.ui_state.teleport_buttons['Basilisk'].disabled = False
            elif new_scene_name == 'gorgon':
                self.gorgon_world = LevelCreator(self, monster_stats=GORGON_STATS)
                new_scene = self.gorgon_world
                self.ui_state.teleport_buttons['Gorgon'].on_click = lambda: self.player.teleport('gorgon')
                self.ui_state.teleport_buttons['Gorgon'].disabled = False
            elif new_scene_name == 'chimera':
                self.gorgon_world = LevelCreator(self, monster_stats=CHIMERA_STATS)
                new_scene = self.chimera_world
                self.ui_state.teleport_buttons['Chimera'].on_click = lambda: self.player.teleport('chimera')
                self.ui_state.teleport_buttons['Chimera'].disabled = False

        if new_scene_name != old_scene_name:
            new_scene.enable()
            old_scene.disable()

        print_on_screen(f'--{new_scene_name.title()}--', position=(-0.1,0.45), scale=3, duration=2)


class GameState():
    def __init__(self):
        self.debug_mode = False

class UIState(Entity):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.damage_text = Text(parent=camera.ui, text='', position=(-0.85,-.22,0), size=0.06)
        self.player_health_bar = HealthBar(max_value=20,value=20,position=(-0.85, -0.39,0),colour=color.red,scale=(0.4,0.05))
        self.player_gold_bar = HealthBar(max_value=10,value=0,position=(-0.85, -0.33,0),colour=color.gold,scale=(0.4,0.05))
        self.player_experience_bar = HealthBar(max_value=10, value=0, position=(-0.89, -0.45,0), colour=color.green, scale=(1.8, 0.05))
        self.level_display = Text(parent=camera.ui, text=1, position=(0, -0.35), size=0.12, font='Assets/Fonts/barber-chop/BarberChop.otf', color=color.lime)
        self.level_display.scale = 0.5
        self.death_screen_background = Entity(parent=camera.ui, model='quad', color=(255,0,0, 0.4), scale=(2,2), position=(0,0,-1), enabled=False)
        self.death_menu = MainMenu(None, None, bg=self.death_screen_background, header='You Died', text='Respawn', enabled=False)

        self.teleport_hud = Panel(parent=camera.ui, color=color.black, enabled=False, scale=(0.7,0.6), position=(0,0,1))
        self.teleport_hud_text = Text(parent=self.teleport_hud, text='Teleport to the following', color=color.red, text_scale=10, origin=(0,0,0), position=(0,0.4,-1))
        self.teleport_buttons = {
            'Tutorial': Button(parent=self.teleport_hud, text='Tutorial', text_size=2, color=color.lime, scale=(0.6,0.15), position=(0,0.3,-1)),
            'Market': Button(parent=self.teleport_hud, text='Market', text_size=2, color=color.lime, scale=(0.6,0.15), position=(0,0.1,-1), disabled=True),
            'Centaur': Button(parent=self.teleport_hud, text='Centaur', text_size=2, color=color.lime, scale=(0.6,0.15), position=(0,-0.1,-1), disabled=True),
            'Basilisk': Button(parent=self.teleport_hud, text='Basilisk', text_size=2, color=color.lime, scale=(0.6,0.15), position=(0,-0.3,-1), disabled=True),
            'Gorgon': Button(parent=self.teleport_hud, text='Gorgon', text_size=2, color=color.lime, scale=(0.6,0.15), position=(0,-0.5,-1), disabled=True),
            'Chimera': Button(parent=self.teleport_hud, text='Chimera', text_size=2, color=color.lime, scale=(0.6,0.15), position=(0,-0.7,-1), disabled=True)}

    def death_screen(self):
        mouse.locked = False
        self.death_menu.enabled = True
        self.death_menu.background.enabled = True
        application.paused = True

    def update(self):
        if self.player != None:
            self.teleport_buttons['Tutorial'].on_click = lambda: self.player.teleport('tutorial')
            self.player_gold_bar.max_value = self.player.max_gold
            self.player_gold_bar.value = self.player.gold
            self.player_health_bar.max_value = self.player.max_health
            self.player_health_bar.value = round(self.player.health)
            self.player_experience_bar.max_value = self.player.levelup_req
            self.player_experience_bar.value = self.player.xp
            self.damage_text.text = f'Damage: {self.player.damage}'
            self.level_display.text = self.player.level
            self.teleport_buttons['Chimera'].on_click = lambda: self.player.teleport('chimera')
            self.teleport_buttons['Chimera'].disabled = False

            if self.player.health <= 0 and not self.death_menu.enabled:
                if self.death_menu.start_function is None:
                    self.death_menu.start_function = self.player.death
                self.death_screen()
            
    def input(self, key):
        if key == 't':
            self.teleport_hud.enabled = not self.teleport_hud.enabled
            mouse.locked = not self.teleport_hud.enabled


class Player(Entity):
    def __init__(self, ui_state, manager):
        super().__init__(model='cube', scale=(1,2.5,1), position=(0,1,0),
                         collider='box', visible_self=manager.debug_mode,
                         color=color.orange)

        self.ui_state = ui_state
        self.manager = manager

        self.speed = 10
        self.default_speed = self.speed
        self.jump_height = 30
        self.gravity = 9.81**2
        self.velocity_y = 0
        self.armor = 0
        self.health = 20
        self.max_health = self.health
        self.damage = 100
        self.level = 1
        self.old_req = 3
        self.levelup_req = 5
        self.xp = 0
        self.stamina = 5
        self.max_stamina = self.stamina
        self.gold = 0
        self.max_gold = 10
        self.inventory = None
        self.basereach = 2
        self.distance = float('inf')
        
        camera.position = (0,1,0)
        camera.rotation = (0,0,0)
        camera.parent = self
        camera.fov = 100
        mouse.locked = True

        self.hand = Entity(model='Assets/Models/Hands/handv5.fbx',texture='Assets/Models/Hands/skin.jpg',
                            parent=self, scale=0.05, collider='box',position=(1,0.5, -1), rotation=(1,1,-25), double_sided = True)

    def death(self):
        application.paused = False
        self.position = Vec3(0,10,0)
        self.max_health = self.max_health - self.level * 2 if self.max_health - self.level*2 >= 20 else self.max_health
        self.health = self.max_health
        self.xp =self.xp // 2
        if self.level > 1:
            self.level -= 1
            self.levelup_req /= 2
            self.levelup_red = round(self.levelup_req)
            self.damage -= 1

        self.ui_state.death_menu.enabled = False
        self.ui_state.death_menu.background.enabled = False
        mouse.locked = True

        if self.manager.location != 'tutorial':
            scenes = f'{self.manager.location}.market'
            manager.switch_scenes(scenes)
    
    def check_max_gold(self):
        if self.gold >= self.max_gold:
            self.gold=self.max_gold
    
    def check_max_health(self):
        if self.health >= self.max_health:
            self.health = self.max_health

    def levelup(self):
        """."""
        self.max_health += self.level * 2
        self.health = self.max_health
        self.xp -= self.levelup_req
        self.level += 1
        self.old_req, self.levelup_req = self.levelup_req, self.old_req + self.levelup_req
        self.max_stamina += 2
        self.damage += 1
        self.armor += 0.5
        self.basereach += 0.1
    
    def teleport(self, location):
        self.ui_state
        manager.switch_scenes(f'{self.manager.location}.{location}')

    def update(self):
        """."""
        if self.xp >= self.levelup_req:
            self.levelup()
        
        self.check_max_gold()
        self.check_max_health()

        # Allow jumping only when the player is on the ground
        ground_ray = raycast(self.position + Vec3(0,0.5,0), direction=Vec3(0,-1,0), distance=2, ignore=[self], debug=self.manager.debug_mode)
        self.grounded = ground_ray.hit
        
        if self.grounded:
            #if self.velocity_y <= 0:
            #    self.y = ground_ray.point.y
            #    self.velocity_y = 0
            self.velocity_y = max(0, self.velocity_y)
            if held_keys['space']:
                self.velocity_y = self.jump_height
        else:
            self.velocity_y -= self.gravity * time.dt
        
        self.y += self.velocity_y * time.dt
        
        # Double speed while sprinting
        if held_keys['left shift']:
            self.speed = self.default_speed * 2
        else:
            self.speed = self.default_speed
        
        # Move the camera to keep up with where the player is watching
        if mouse.locked:
            camera.rotation_x -= mouse.velocity[1] * 80
            self.rotation_y += mouse.velocity[0] * 80
            camera.rotation_x = min(max(-90, camera.rotation_x), 90)

        # Handle the player movement
        movement = Vec3(self.forward * (held_keys['w'] - held_keys['s'])
                        + self.right * (held_keys['d'] - held_keys['a'])).normalized()
        
        # Change hitbox colours when colliding for testing purposes
        dictionary = {'tutorial': manager.tutorial_world,
                      'market': manager.market_world,
                      'centaur': manager.centaur_world,
                      'basilisk': manager.basilisk_world,
                      'gorgon': manager.gorgon_world}

        colliders = dictionary[self.manager.location].colliders
        if self.manager.debug_mode:
            for collider in colliders:
                if self.intersects(collider).hit:
                    collider.color = color.red
                else:
                    collider.color = color.white
        
        # Check if nothing is infront of the player before moving
        ignore = [self, self.hand]
        hit_info = raycast(self.world_position, movement, distance=0.5, debug=self.manager.debug_mode, ignore=ignore)
        if not hit_info.hit:
            move_amount = movement * self.speed * time.dt
            self.position += move_amount
        else:
            name = hit_info.entity.name
            if name.startswith('gate') and name.split('.')[-1] == 'complete':
                scenes = name[5:]
                manager.switch_scenes(scenes)

        
class Monster(Entity):
    def __init__(self, manager, parent, monster_stats, is_boss=False, is_tutorial=False, gate=None, position=Vec3(0,0,0), rotation=Vec3(0,0,0), boss_type='fbx', scale=1, enabled=True):
        super().__init__(model=f'Assets/Models/{monster_stats["name"]}/base_monster.fbx',
                       texture=f'Assets/Models/{monster_stats["name"]}/texture.png',
                       position=position, double_sided=True, scale=monster_stats['scale']*scale,
                       rotation=rotation, name=monster_stats["name"], parent=parent, enabled=enabled,
                       shader=unlit_shader, cache_compiled_model=False)

        self.collision_box = Entity(model='cube', parent=self, position=monster_stats['collider_position'],
                                    scale=monster_stats['collider_scale'], visible=manager.debug_mode,
                                    wireframe=True, name=f'{monster_stats["name"]}.collider')

        self.parent = parent
        self.monster_stats = monster_stats
        self.name = monster_stats['name']
        self.health = monster_stats['health']
        self.max_health = monster_stats['health']
        self.damage = monster_stats['damage']
        self.sight = monster_stats['sight']
        self.worth = monster_stats['worth']
        self.speed = monster_stats['speed']
        self.attack_speed = monster_stats['attack_speed']
        self.closeness = monster_stats['closeness']
        self.position = position
        self.origin_position = position
        self.scale = monster_stats['scale']
        self.rotation = rotation
        self.origin_rotation = rotation
        self.is_boss = is_boss
        self.is_boss_true = is_boss
        self.is_tutorial = is_tutorial
        self.gate = gate

        if self.is_boss:
            self.model = f'Assets/Models/{self.name}/Boss/boss.{boss_type}'
            self.texture = f'Assets/Models/{self.name}/Boss/texture.png'
            self.scale = monster_stats['boss_scale']
            self.collision_box.scale = monster_stats['boss_collider_scale']
            self.collision_box.position = monster_stats['boss_collider_pos']
            self.speed = monster_stats['boss_speed']
            self.closeness = monster_stats['boss_closeness']
            self.sight = monster_stats['boss_sight']
            self.boss_rotation = monster_stats['boss_rotation']
            self.origin_rotation = self.boss_rotation
            self.damage *= 2
            self.health *= 5
            self.max_health = self.health
            self.worth *= 10

    def death(self):
        self.visible = False
        self.collision_box.visible = False
        self.enabled = False
        self.collision_box.enabled = False
        self.ignore = True
        self.collision_box.ignore = True
        self.is_boss = False
        self.is_tutorial = False
        invoke(self.respawn, delay=self.monster_delay)
    
    def respawn(self):
        self.position = self.origin_position
        self.rotation = self.origin_rotation
        self.visible = True
        self.collision_box.visible = True
        self.enabled = True
        self.collision_box.enabled = True
        self.ignore = False
        self.collision_box.ignore = False
        self.health = self.max_health

    def on_click(self):
        """This triggers when the mouse clicks the monster."""
        self.distance = distance(self, manager.player)
        if self.distance <= manager.player.basereach + self.closeness:
            self.health -= manager.player.damage

            # Flash Red Effect
            self.blink(color.red)
            
            if self.health <= 0:
                self.monster_delay = 10
                if self.is_boss_true:
                    print_on_screen(f'<red>{self.name.title()} boss Defeated!', position=(-0.4,0.4), scale=3, duration=2)
                    self.monster_delay=60
                if self.is_boss or self.is_tutorial:
                    self.gate.portal.animate('alpha', 1, duration=1, curve=curve.in_out_sine)
                    self.gate.pattern.animate_color(color.green,duration=1, curve=curve.in_out_sine)
                    self.gate.complete = True
                    self.gate.name = f'{self.gate.name[:-10]}complete'
                    self.gate.collision_box.name = self.gate.name
                    camera.shake(duration=1)
                manager.player.gold += self.worth
                manager.ui_state.player_gold_bar.value += self.worth
                manager.player.xp += self.worth
                manager.ui_state.player_experience_bar.value += self.worth
                self.death()

    def update(self):
        """."""
        self.distance = distance(self, manager.player)
        if self.closeness < self.distance <= self.sight:
            self.look_at_2d(manager.player, 'y')
            #self.position += self.forward * time.dt * self.speed
            if self.is_boss:
                self.rotation_y += self.boss_rotation

        if self.distance <= self.closeness:
            damage_delt = self.damage - manager.player.armor
            if damage_delt >= 1:
                manager.player.health -= damage_delt * time.dt * self.attack_speed

    def input(self, key):
        if key == 'left mouse up':
            self.on_click()


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

class Gate(Entity):
    def __init__(self, manager, position, locations, parent, complete=False, scale=(0.002,0.004,0.002), rotation_y=0):
        super().__init__(parent=parent, complete=complete, position=(0,-1,0))

        self.complete = complete
        self.name = f'gate.{locations}.incomplete' if not self.complete else f'gate.{locations}.complete'
        

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


class Stall(Entity):
    def __init__(self, manager, parent):
        super().__init__(parent=parent,model='Assets/Models/Stall/Stall/stall1.fbx', texture='Assets/Models/Stall/Stall/stall_texture.png',
                         double_sided=True, scale=(0.1,0.22,0.1), position=(10,0,0))

        self.props = Entity(model='Assets/Models/Stall/Props/props.fbx', texture='Assets/Models/Stall/Props/props_texture.png',
                            parent=self, double_sided=True,scale=(1,1,1), position=(0,0,0))

        self.collision_box = Entity(model='cube', parent=self, name=self.name,
                                    position=(0,0,0), scale=(40,50,40),
                                    collider='box', visible=manager.debug_mode,
                                    wireframe=True)
        self.merchant = Entity(model='Assets/Models/Stall/Merchant/merchant.fbx', texture='Assets/Models/Stall/Merchant/texture.jpg',
                               double_sided=True, parent=self, scale=(.11,.11,.11), position=(0,0,0))

class CentaurMap(Entity):
    def __init__(self, manager, parent):
        super().__init__(parent=parent, model='Assets/Models/Centaur/World/ground.fbx', texture='Assets/Models/Centaur/World/ground.png',
                         double_sided=True, scale=(.05,.05,.05), position=(5,0,80), rotation_y=90)
        
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
        

class GorgonMap(Entity):
    def __init__(self, parent):
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
        self.cubes() 
    
class ChimeraMap(Entity):
    def __init__(self):
        super().__init__()

class GridCube(Draggable):
    def __init__(self, pos):
        super().__init__(
            parent=scene, 
            model='cube', 
            color=color.white, 
            scale=1, 
            plane_direction=(0,1,0), 
            position=pos
        )

    def drag(self):
        self.color = color.red
        print(f"Picked up at: {self.position}")

    def drop(self):
        self.color = color.azure
        print(f"Dropped at: {self.position}")

    def cubes(self):
        for x in range(10):
            for z in range(10):
                GridCube(pos=(x, 1, z))
  

class TutorialWorld(Entity):
    def __init__(self, manager):
        super().__init__()
        self.ground = Entity(parent=self,model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))

        self.wall = Entity(parent=self,model='Assets/Models/Wall/wall.fbx', texture='Assets/Models/Wall/texture.png',
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
        
        self.wall = Entity(parent=self,model='Assets/Models/Wall/wall.fbx', texture='Assets/Models/Wall/texture.png',
                    double_sided=True,scale=(0.01,0.01,0.01), collider='mesh', position=(-30,5,-10))

        self.tutorial_gate = Gate(manager, parent=self, position=(0,-0.7,-5), locations='market.tutorial', complete=True, rotation_y=180)
        self.centaur_gate = Gate(manager, parent=self, position=(0,-0.7,20), locations='market.centaur', complete=True)

        self.stall = Stall(manager,parent=self)

        self.colliders = [self.tutorial_gate.collision_box, self.stall.collision_box, self.centaur_gate.collision_box]

class LevelCreator(Entity):
    def __init__(self, manager, monster_stats):
        super().__init__()

        self.name = monster_stats['name']

        self.location = manager.location

        self.next_scene = manager.locations.index(self.location.title()) + 1
        self.next_scene = manager.locations[self.next_scene].lower()
        
        self.previous_scene = manager.locations.index(self.location.title()) - 1
        self.previous_scene = manager.locations[self.previous_scene].lower()
        
        if self.name == 'Centaur':
            self.world = CentaurMap(manager, self)
            self.x_multi = 8
            self.x_add = -60
            self.z_multi = 8
            self.z_add = -10
            self.boss_type = 'fbx'
        elif self.name == 'Basilisk':
            self.world = BasiliskMap(manager, self)
            self.x_multi = 2
            self.x_add = -36.5
            self.z_multi = 2
            self.z_add = -3
            self.boss_type = 'obj'
        elif self.name == 'Gorgon':
            self.world = GorgonMap(parent=self)
            self.x_multi = 1
            self.x_add = 0
            self.z_multi = 1
            self.z_add = 0
            self.boss_type = 'fbx'

        if hasattr(self.world, 'map') and self.world.map:
            self.world.map.reverse()
            for z, row in enumerate(self.world.map):
                for x, col in enumerate(row):
                    position = ((x*self.x_multi)+self.x_add,0,(z*self.z_multi)+self.z_add)
                    if col == 'M':
                        
                        Monster(manager, parent=self, monster_stats=monster_stats, position=position, rotation=(0,random.randint(-360,360),0))
                    elif col == 'O':
                        self.next_gate = Gate(manager, parent=self, position=(position[0], self.world.out_position, position[2]), locations=f'{self.location}.{self.next_scene}')
                    elif col == 'I':
                        self.return_gate = Gate(manager, parent=self, position=position, locations=f'{self.location}.{self.previous_scene}', complete=True, rotation_y=180)
                    elif col == 'B':
                        self.boss = Monster(manager, parent=self, monster_stats=monster_stats, is_boss=True, gate=None, position=position, boss_type=self.boss_type)

        elif hasattr(self.world, 'positions'):
            for position in self.world.positions:
                Monster(manager, parent=self, monster_stats=monster_stats, position=position, rotation=(0,random.randint(-360,360),0))
    
            self.next_gate = Gate(manager, parent=self, position=self.world.next_gate_position, locations=f'{self.location}.{self.next_scene}')
            self.return_gate = Gate(manager, parent=self, position=(0,0,-5), locations=f'{self.location}.{self.previous_scene}', complete=True, rotation_y=180)
            self.boss = Monster(manager, parent=self, monster_stats=monster_stats, is_boss=True, gate=None, position=self.world.boss_position, boss_type=self.boss_type)
        else:
            self.next_gate = Gate(manager, parent=self, position=(0,0,10), locations=f'{self.location}.{self.next_scene}')
            self.return_gate = Gate(manager, parent=self, position=(0,0,-2), locations=f'{self.location}.{self.previous_scene}', complete=True, rotation_y=180)
            self.boss = Monster(manager, parent=self, monster_stats=monster_stats, is_boss=True, gate=None, position=(0,0,8))

        self.boss.gate = self.next_gate

        self.colliders = [self.return_gate.collision_box, self.next_gate.collision_box]

#---------------------------------------------------#
def spectator_input(key):
    if key == 'tab' and main_menu.started:
        spectator_mode.enabled = not spectator_mode.enabled
        spectator_mode.position = manager.player.position
        application.paused = spectator_mode.enabled
        camera.parent = spectator_mode if spectator_mode.enabled else manager.player

#------------------------------------------------------------#

app = Ursina()

window.icon = 'Assets/ursina.ico'
spectator_mode = EditorCamera(enabled = False, ignore_paused=True)
pause_handler = Entity(ignore_paused=True, input=spectator_input)
manager = GameManager()
main_menu = MainMenu(manager.start_game, manager.resume_game)

def input(key):
    if key == 'c' and hasattr(manager, 'debug_mode'):
        manager.debug_mode = not manager.debug_mode

def update():
    if held_keys['escape']:
        manager.pause_game()
    if manager.player is not None:
        if held_keys['g']:
            manager.player.gold += 1
        if held_keys['x']:
            manager.player.xp += 100

app.run()
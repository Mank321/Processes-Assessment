from ursina import *
from Scripts.HealthBar import HealthBar
from Scripts.MainMenu import MainMenu


class GameManager(Entity):
    """."""
    def __init__(self):
        """."""
        super().__init__()
        self.player = None
        self.ui_state = None 
        self.game_state = None
        self.tutorial_world = None
        self.market_world = None

    def start_game(self):
        """."""
        main_menu.started = True
        main_menu.enabled = False
        main_menu.background.enabled = False
        
        # Initialize the main classes
        self.game_state = GameState()
        self.ui_state = UIState(self.game_state, None)
        self.player = Player(self.ui_state, self.game_state)
        self.ui_state.player = self.player         

        # Load the tutorial world at the beginning 
        self.tutorial_world = TutorialWorld(self.game_state)

        self.game_state.location = 'tutorial'
        self.sky = Sky()


    def pause_game(self):
        mouse.locked = False
        main_menu.start_buttons.enabled = False
        main_menu.pause_buttons.enabled = True
        main_menu.background.enabled = True
        main_menu.enabled = True
        for entity in self.ui_state.entities:
            entity.disable()

    def resume_game(self):
        main_menu.enabled = False
        main_menu.background.enabled = False
        mouse.locked = True
        for entity in self.ui_state.entities:
            entity.enable()
    
    def switch_scenes(self, gate):
        """."""
        new_scene = gate.name.split('.')[2]
        old_scene = gate.name.split('.')[1]
        scene = old_scene.gate.name.split('.')[1]

        if new_scene == None:
            if scene == 'market':
                self.market_world = MarketWorld(self.game_state)
                new_scene = self.market_world
            
        new_scene.enable()
        for entity in new_scene.entities:
            entity.enable()
        for entity in new_scene.colliders:
            entity.enable()
        old_scene.disable()

        print_on_screen(f'--{scene.title()}--', position=(-0.1,0.45), scale=3, duration=2)
        self.game_state.location = scene
        self.player.position = (0,0,0)
        self.player.rotation = (0,0,0)


class GameState():
    def __init__(self):
        self.debug_mode = True

class UIState(Entity):
    def __init__(self, game_state, player):
        super().__init__()
        self.player = player
        self.game_state = game_state
        #self.coordinate_text = Text(self.player, position=(0,0), parent=camera.ui)
        self.player_health_bar = HealthBar(max_value=20,value=20,position=(-0.85, -0.4),colour=color.red,scale=(0.4,0.05))
        self.player_gold_bar = HealthBar(max_value=10,value=0,position=(-0.85, -0.35),colour=color.gold,scale=(0.4,0.05))

        self.entities = [self.player_health_bar, self.player_gold_bar]#self.coordinate_text, ]

    def update(self):
        if self.player != None:
            self.player_gold_bar.max_value = self.player.max_gold
            self.player_gold_bar.value = self.player.gold
        #self.coordinate_text.text = self.player.position if self.player != None else ''

class Player(Entity):
    def __init__(self, ui_state, game_state):
        super().__init__(model='cube', scale=(1,2.5,1), position=(0,1,0),
                         collider='box', visible_self=game_state.debug_mode,
                         color=color.orange)

        self.ui_state = ui_state
        self.game_state = game_state

        self.speed = 10
        self.default_speed = self.speed
        self.jump_height = 30
        self.gravity = 9.81**2
        self.velocity_y = 0
        self.armor = 0
        self.health = 20
        self.max_health = self.health
        self.damage = 1
        self.level = 1
        self.levelup_req = 10 * self.level
        self.xp = 0
        self.stamina = 5
        self.gold = 0
        self.max_gold = 10
        self.inventory = None
        self.reach = 5
        self.distance = float('inf')

        self.transition_cooldown = 0
        self.move_sequence = None
        
        camera.position = (0,1,0)
        camera.rotation = (0,0,0)
        camera.parent = self
        camera.fov = 100
        mouse.locked = True

        self.hand = Entity(model='Assets/Models/Hands/handv5.fbx',texture='Assets/Models/Hands/skin.jpg',
                            parent=self, scale=0.05, collider='box',position=(1,0.5, -1), rotation=(1,1,-25), double_sided = True)

    def death(self):
            self.position = Vec3(0,10,0)
            self.health = self.max_health
            self.ui_state.player_health_bar.value = self.max_health
            #if manager.game_state.location != 'tutorial world':
            #    manager.switch_scenes(manager.market_world, manager.)

    def update(self):
        """."""
        # A cooldown for using the gates
        if self.transition_cooldown > 0:
            self.transition_cooldown -= time.dt
        
        # Allowing jumping only when the player is on the ground
        ground_ray = raycast(self.world_position + Vec3(0,0.1,0), self.down, distance=1.1, ignore=[self])
        self.grounded = ground_ray.hit
        
        if self.grounded:
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
        camera.rotation_x -= mouse.velocity[1] * 80
        self.rotation_y += mouse.velocity[0] * 80
        camera.rotation_x = min(max(-90, camera.rotation_x), 90)

        # Handle the player movement
        movement = Vec3(self.forward * (held_keys['w'] - held_keys['s'])
                        + self.right * (held_keys['d'] - held_keys['a'])).normalized()
        
        # Change hitbox colours when colliding for testing purposes
        dictionary = {'tutorial': manager.tutorial_world,
                'market': manager.market_world}
        colliders = dictionary[self.game_state.location].colliders
        if self.game_state.debug_mode:
            for collider in colliders:
                if self.intersects(collider).hit:
                    collider.color = color.red
                else:
                    collider.color = color.white
        
        # Check if nothing is infront of the player before moving
        ignore = [self, self.hand]
        hit_info = raycast(self.world_position, movement, distance=0.1, debug=True, ignore=ignore)
        if not hit_info.hit:
            move_amount = movement * self.speed * time.dt
            self.position += move_amount
        else:
            name = hit_info.entity.name
            if name.startswith('gate'):
                manager.switch_scenes(hit_info.entity)

        if self.health <= 0:
            self.death()
                
        
        
class Monster(Entity):
    def __init__(self, game_state, parent,name='monster', health=10, damage=1, worth=1, speed=50, sight=10, position=Vec3(0,0,0), scale=1, rotation=Vec3(0,0,0)):
        super().__init__(model=f'Assets/Models/{name.title()}/{name}.fbx',
                       texture=f'Assets/Models/{name.title()}/texture.png',
                       position=position, double_sided=True, scale=scale,
                       rotation=rotation, name=name, parent=parent)

        self.collision_box = Entity(model='cube', parent=self, position=(0,200,0),
                                    scale=(100,400,170), collider='box',
                                    visible=game_state.debug_mode,
                                    wireframe=True, name=f'{name}.collider')
        
        self.name = name
        self.health = health
        self.damage = damage
        self.position = position
        self.scale = scale
        self.rotation = rotation
        self.speed = speed
        self.closeness = 2
        self.sight = sight
        self.worth = worth

        self.game_state = game_state

    def distance_check(self):
        """."""
        self.distance = distance(self, manager.player)
        if self.closeness < self.distance <= self.sight:
            self.look_at_2d(manager.player, 'y')
            self.position += self.forward * time.dt * self.speed

        if self.distance <= self.closeness:
            invoke(setattr, manager.player, 'health', manager.player.health - self.damage, delay=1)
            manager.ui_state.player_health_bar.value = manager.player.health

    def on_click(self):
        """This triggers when the mouse clicks the monster."""
        self.distance = distance(self, manager.player)
        if self.distance <= manager.player.reach:
            self.health -= manager.player.damage

            # Flash Red Effect
            origin_colour = self.color
            self.color = color.red
            self.animate_color(origin_colour, duration=0.2)
            
            if self.health <= 0:
                if self.game_state.location == 'tutorial world':
                    manager.tutorial_world.entities.remove(self)
                    manager.tutorial_world.colliders.remove(self.collision_boxwwww)
                destroy(self)
                manager.player.gold += self.worth
                manager.ui_state.player_gold_bar.value += self.worth

    def update(self):
        self.distance_check()

    def input(self, key):
        if key == 'left mouse up':
            self.on_click()


class LevelCreator():
    def __init__(self):
        pass

class Tree(Entity):
    def __init__(self, game_state, position, parent):
        super().__init__(model='Assets/Models/Tree/treev2.fbx',
                         texture='Assets/Models/Tree/texture.png',
                         scale=(0.05,0.04,0.05), position=position,
                         double_sided=True, name='tree', parent=parent)

        self.collision_box = Entity(model='cube', parent=self,
                                    position=(0,125,0), scale=(70,250,70),
                                    collider='box', visible=game_state.debug_mode,
                                    wireframe=True)

class Gate(Entity):
    def __init__(self, game_state, position, name, parent):
        super().__init__(parent=parent,model='Assets/Models/Gate/gate.fbx', texture='Assets/Models/Gate/texture.png',
                         double_sided=True, scale=(0.02,0.03,0.015), rotation_y=180, position=position)
        
        self.name = name
        self.collision_box = Entity(model='cube', parent=self, name=self.name,
                                    position=(0,150,0), scale=(200,300,100),
                                    collider='box', visible=game_state.debug_mode,
                                    wireframe=True)

class Stall(Entity):
    def __init__(self, game_state, parent):
        super().__init__(parent=parent,model='Assets/Models/Stall/stall1.fbx', texture='Assets/Models/Stall/stall_texture.png',
                         double_sided=True,scale=(0.1,0.22,0.1), position=(10,0,0))

        self.props = Entity(model='Assets/Models/Stall/props.fbx', texture='Assets/Models/Stall/props_texture.png',
                            parent=self, double_sided=True,scale=(1,1,1), position=(0,0,0))

        self.collision_box = Entity(model='cube', parent=self, name=self.name,
                                    position=(0,0,0), scale=(40,50,40),
                                    collider='box', visible=game_state.debug_mode,
                                    wireframe=True)
        self.merchant = Entity()
        

class TutorialWorld(Entity):
    def __init__(self, game_state):
        super().__init__()
        #self.game_state = game_state
        self.ground = Entity(parent=self,model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))

        self.wall = Entity(parent=self,model='Assets/Models/Wall/wall.fbx', texture='Assets/Models/Wall/texture.png',
                    double_sided=True,scale=(0.005,0.01,0.005), collider='mesh', position=(0,5,10))
        
        self.gate = Gate(game_state, parent=self, position=(0,0,30), name='gate.tutorial.market')

        self.desc1 = '             Welcome to the dungeon!\n\nUse the mouse to move around\nPress "W" to move forward, "S" to move backward\nPress "A" to move right and "D" to move left\nPress the spacebar to jump'
        self.text1 = Text(parent=self, text=self.desc1, position=(-8,5,9), scale=30, color=color.white)
        
        self.desc2 = 'Attack the monster up ahead by left clicking!\n                     Try not to get hit!'
        self.text2 = Text(parent=self, text=self.desc2, position=(-8,4,19), scale=30, color=color.white)

        self.monster = Monster(game_state, parent=self,name='centaur', health=10,
                               damage=1, position=Vec3(0,0,25),
                               scale=Vec3(0.02,0.024,0.015),
                               rotation=Vec3(0,180,0))
        
        #self.entities = [self.ground, self.wall, self.gate, self.text1, self.text2, self.monster]
        self.colliders = [self.gate.collision_box]#, self.monster.collision_box]
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
                    Tree(game_state, ((x*4)-45, 0, (z*4)-7),parent=self)
                    #self.entities.append(tree)
                    #self.colliders.append(tree.collision_box)
                    #self.entities.append(tree.collision_box)


class MarketWorld(Entity):
    def __init__(self, game_state):
        super().__init__()
        self.ground = Entity(parent=self,model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))
        
        self.wall = Entity(parent=self,model='Assets/Models/Wall/wall.fbx', texture='Assets/Models/Wall/texture.png',
                    double_sided=True,scale=(0.01,0.01,0.01), collider='mesh', position=(-30,5,-10))

        self.tutorial_gate = Gate(game_state, parent=self,position=(0,0,-5), name='gate.market.tutorial')
        self.centaur_gate = Gate(game_state, parent=self,position=(0,0,-10), name='gate.market.centaur')

        self.stall = Stall(game_state,parent=self)

        self.entities = [self.ground, self.wall, self.tutorial_gate, self.tutorial_gate.collision_box, self.centaur_gate, self.centaur_gate.collision_box, self.stall, self.stall.collision_box]
        self.colliders = [self.tutorial_gate.collision_box, self.stall.collision_box, self.centaur_gate.collision_box]

#---------------------------------------------------#
def update():
    if held_keys['escape']:
        manager.pause_game()

def pause_input(key):
    if key == 'tab' and main_menu.started:
        spectator_mode.enabled = not spectator_mode.enabled
        #mouse.locked = spectator_mode.enabled
        spectator_mode.position = manager.player.position
        
        application.paused = spectator_mode.enabled
        
        camera.parent = spectator_mode if spectator_mode.enabled else manager.player

#------------------------------------------------------------#

app = Ursina()

window.icon = 'Assets/ursina.ico'
spectator_mode = EditorCamera(enabled = False, ignore_paused=True)
pause_handler = Entity(ignore_paused=True, input=pause_input)
manager = GameManager()
main_menu = MainMenu(manager.start_game, manager.resume_game)

app.run()
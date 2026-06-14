from ursina import *
from Scripts.MainMenu import MainMenu

class GameManager(Entity):
    """."""
    def __init__(self):
        """."""
        super().__init__()
        self.player = None
        self.ui_state = None 
        self.game_state = None

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
        self.load_tutorial()

        self.sky = Sky()


    def pause_game(self):
        mouse.locked = False
        main_menu.start_buttons.enabled = False
        main_menu.pause_buttons.enabled = True
        main_menu.background.enabled = True
        main_menu.enabled = True

    def resume_game(self):
        main_menu.enabled = False
        main_menu.background.enabled = False
        mouse.locked = True

    def load_tutorial(self):
        if hasattr(self.game_state, 'market_entities'):# and self.game_state.market_entities not None:
            for entity in self.game_state.market_entities:
                entity.disable()
            for entity in self.game_state.market_collisions:
                entity.disable()
        if hasattr(self.game_state, 'tutorial_entities'):
            for entity in self.game_state.tutorial_entities:
                entity.enable()
            for entity in self.game_state.tutorial_collisions:
                entity.enable()
        else:
            create_tutorial_world(self.game_state, self.player)

        self.game_state.location = 'tutorial'
        self.player.position = (0,0,0)
    
    def load_market(self):
        if self.game_state.location == 'tutorial':
            for entity in self.game_state.tutorial_entities:
                entity.disable()
            for entity in self.game_state.tutorial_collisions:
                entity.disable()
        if hasattr(self.game_state, 'market_entities'):
            for entity in self.game_state.market_entities:
                entity.enable()
            for entity in self.game_state.market_collisions:
                entity.enable()
        else:
            create_market_world(self.game_state)
        self.game_state.location = 'market'
        self.player.position = (0,0,0)

class GameState():
    def __init__(self):
        self.debug_mode = True

class UIState():
    def __init__(self, game_state, player):
        self.player = player
        self.game_state = game_state
        self.coordinate_text = Text(self.player, position=(0,0), parent=camera.ui)
        self.entities = [self.coordinate_text]
    
    def update(self):
        self.coordinate_text.text = self.player.position if self.player != None else ''
        print(self.coordinate_text.text)
        print('hi')

class Player(Entity):
    def __init__(self, ui_state, game_state):
        super().__init__(model='cube', scale=(1,2,1), position=(0,1,0),
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
        self.inventory = None

        self.transition_cooldown = 0
        self.move_sequence = None
        
        camera.position = (0,1,0)
        camera.rotation = (0,0,0)
        camera.parent = self
        camera.fov = 100
        mouse.locked = True
    
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
        if hasattr(self.game_state, 'tutorial_colliders') and self.game_state.debug_mode:
            for collider in self.game_state.tutorial_colliders:
                if self.intersects(collider).hit:
                    collider.color = color.red
                else:
                    collider.color = color.white
        
        # Check if nothing is infront of the player before moving
        ignore = [self, self.hand] if hasattr(self, 'hand') else [self]
        hit_info = raycast(self.world_position, movement, distance=0.1, debug=True, ignore=ignore)
        if not hit_info.hit:
            move_amount = movement * self.speed * time.dt
            self.position += move_amount
        else:
            name = hit_info.entity.name
            if name.startswith('gate'):
                new_location = name.split('.')[1]
                if new_location == 'market':
                    manager.load_market()
                elif new_location == 'tutorial':
                    pass
        
        
class Monster(Entity):
    def __init__(self, name, health, damage, speed=5):
        pass

class LevelCreator():
    def __init__(self):
        pass

class Tree(Entity):
    def __init__(self, game_state, position):
        super().__init__(model='Assets/Models/Tree/treev2.fbx',
                         texture='Assets/Models/Tree/texture.png',
                         scale=(0.05,0.04,0.05), position=position,
                         double_sided=True, name='tree')

        self.collision_box = Entity(model='cube', parent=self,
                                    position=(0,125,0), scale=(70,250,70),
                                    collider='box', visible=game_state.debug_mode,
                                    wireframe=True)

class Gate(Entity):
    def __init__(self, game_state, position, name):
        super().__init__(model='Assets/Models/Gate/gate.fbx', texture='Assets/Models/Gate/texture.png',
                         double_sided=True, scale=(0.02,0.03,0.015), rotation_y=180, position=position)

        self.collision_box = Entity(model='cube', parent=self, name=name,
                                    position=(0,150,0), scale=(200,300,100),
                                    collider='box', visible=game_state.debug_mode,
                                    wireframe=True)
#---------------------------------------------------#

def create_tutorial_world(game_state, player):
    ground = Entity(model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))
    player.hands = Entity(model='Assets/Models/Hands/handv5.fbx',texture='Assets/Models/Hands/skin.jpg',
                          parent=player, scale=0.05, collider='box',position=(1,0.5, -1), rotation=(1,1,-25), double_sided = True)
    wall = Entity(model='Assets/Models/Wall/wall.fbx', texture='Assets/Models/Wall/texture.png',
                  double_sided=True,scale=(0.01,0.01,0.01), collider='mesh', position=(-30,5,-10))
    
    gate = Gate(game_state, position=(0,0,30), name='gate.market')

    desc = '             Welcome to the dungeon!\n\nUse the mouse to move around\nPress "W" to move forward, "S" to move backward\nPress "A" to move right and "D" to move left\nPress the spacebar to jump'
    text1 = Text(parent=scene, text=desc, position=(-8,5,9), scale=30, color=color.white)
    
    desc = 'Attack the monster up ahead by left clicking!\n                     Try not to get hit!'
    text2 = Text(parent=scene, text=desc, position=(-8,4,19), scale=30, color=color.white)
    
    game_state.tutorial_entities = [ground, wall, gate, text1, text2]
    game_state.tutorial_colliders = [gate.collision_box]
    for i in range(1):
        pos = Vec3(random.randint(-45,45), 0, random.randint(-10,80))
        tree=Tree(game_state, pos)
        game_state.tutorial_entities.append(tree)
        game_state.tutorial_colliders.append(tree.collision_box)
        game_state.tutorial_entities.append(tree.collision_box)
        
    

def update():
    if held_keys['escape']:
        manager.pause_game()

def pause_input(key):
    if key == 'tab':
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
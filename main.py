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
        
        # Set the current level to be tutorial
        self.game_state.location = 'tutorial'

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
        create_tutorial_world(self.game_state, self.player)

class GameState():
    def __init__(self):
        pass

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
        super().__init__(model='cube', scale=(1,2,1), position=(0,1,0), collider='box', visible_self=False)
        self.ui_state = ui_state
        self.game_state = game_state

        self.speed = 10
        self.default_speed = self.speed
        self.jump_height = 500
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
        if self.transition_cooldown > 0:
            self.transition_cooldown -= time.dt
        
        ray = raycast(self.world_position + Vec3(0,0.1,0), self.down, distance=1.1, ignore=[self])
        self.grounded = ray.hit
        
        if self.grounded:
            self.velocity_y = max(0, self.velocity_y)
            if held_keys['space']:
                self.velocity_y = self.jump_height
        else:
            self.velocity_y -= self.gravity * time.dt
        
        self.y += self.velocity_y * time.dt
        
        if held_keys['left shift']:
            self.speed = self.default_speed * 2
        else:
            self.speed = self.default_speed
        
        movement = Vec3(self.forward * (held_keys['w'] - held_keys['s'])
                        + self.right * (held_keys['d'] - held_keys['a'])).normalized()
        
        move_amount = movement * self.speed * time.dt
        self.position += move_amount
        
        camera.rotation_x -= mouse.velocity[1] * 80
        self.rotation_y += mouse.velocity[0] * 80
        camera.rotation_x = min(max(-90, camera.rotation_x), 90)
        
        
class Monster(Entity):
    def __init__(self, name, health, damage, speed=5):
        pass

class LevelCreator():
    def __init__(self):
        pass

#---------------------------------------------------#

def create_tutorial_world(game_state, player):
    ground = Entity(model='plane', collider='box', scale=200, texture='grass', texture_scale=(4,4))
    player.hands = Entity(parent=player, scale=0.05, collider='box',position=(1,0.5, 0), rotation=(1,1,-25),
                   model='Assets/Models/Hands/handv5.fbx',
                   texture='Assets/Models/Hands/skin.jpg', double_sided = True)
    wall = Entity(scale=(0.05,0.1,0.05), collider='box', position=(-150,0,-220),
                  model='Assets/Models/Wall/wall.fbx',
                  texture='Assets/Models/Wall/texture.png', double_sided=True)
    tree = Entity(scale=(0.1,0.1,0.1), position=(5,7,0), collider='box',
                  model='Assets/Models/Tree/tree.fbx',
                  texture='Assets/Models/Tree/texture.png')
    
    
    game_state.tutorial_entities = [ground, wall]

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
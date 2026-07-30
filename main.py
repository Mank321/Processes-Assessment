import random
from ursina import Entity, Sky, application, Text, color, Button, Panel, Ursina, EditorCamera, held_keys, print_on_screen, invoke, mouse, camera, window
from Scripts.HealthBar import HealthBar
from Scripts.MainMenu import MainMenu
from Scripts.Maps import CentaurMap, BasiliskMap, GorgonMap, ChimeraMap
from Scripts.Objects import Gate
from Scripts.Worlds import TutorialWorld, MarketWorld, RebirthWorld
from Scripts.Monster import Monster
from Scripts.Player import Player
from Scripts.Store import Store
from Scripts.MonsterStats import CENTAUR_STATS, BASILISK_STATS, GORGON_STATS, CHIMERA_STATS

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
        self.rebirth_world = None

        self.locations = [
            'Tutorial',
            'Market',
            'Centaur',
            'Basilisk',
            'Gorgon',
            'Chimera',
            'Rebirth',
        ]

        self.location = None
        self.debug_mode = False

    def start_game(self):
        """."""
        main_menu.started = True
        main_menu.enabled = False
        main_menu.background.enabled = False
        
        # Initialize the main classes
        self.store = Store(self)
        self.ui_state = UIState(self, None)
        self.player = Player(self.ui_state, self)
        self.ui_state.player = self.player         

        # Load the tutorial world at the beginning 
        self.tutorial_world = TutorialWorld(self)

        self.location = 'tutorial'
        self.sky = Sky()


    def pause_game(self):
        """."""
        mouse.locked = False
        self.ui_state.teleport_hud.enabled = False
        self.store.enabled = False
        main_menu.start_buttons.enabled = False
        main_menu.pause_buttons.enabled = True
        main_menu.background.enabled = True
        main_menu.enabled = True
        main_menu.background.z = -2
        application.paused = True

    def resume_game(self):
        """."""
        self.player.movement_locked = False
        main_menu.enabled = False
        main_menu.background.enabled = False
        mouse.locked = True
        main_menu.background.z = 1
        application.paused = False

    def switch_scenes(self, gate):
        """."""
        #self.ui_state.loading_hud.enabled=True
        self.player.position = (0,1,0)
        new_scene_name = gate.split('.')[1]
        old_scene_name = gate.split('.')[0]

        if new_scene_name != old_scene_name:
            self.player.movement_locked = True
            self.location = new_scene_name

            self.scenes = {'tutorial': self.tutorial_world, 'market': self.market_world,
                        'centaur': self.centaur_world, 'basilisk': self.basilisk_world,
                        'gorgon': self.gorgon_world, 'chimera': self.chimera_world,
                        'rebirth': self.rebirth_world}

            self.scene_weights = {'tutorial':0,
                                  'market':1,
                                  'centaur':2,
                                  'basilisk':3,
                                  'gorgon':4,
                                  'chimera':5,
                                  'rebirth':6}

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
                    self.chimera_world = LevelCreator(self, monster_stats=CHIMERA_STATS)
                    new_scene = self.chimera_world
                    self.ui_state.teleport_buttons['Chimera'].on_click = lambda: self.player.teleport('chimera')
                    self.ui_state.teleport_buttons['Chimera'].disabled = False
                elif new_scene_name == 'rebirth':
                    self.rebirth_world = RebirthWorld(self)
                    new_scene = self.rebirth_world
                    self.ui_state.teleport_buttons['Rebirth'].on_click = lambda: self.player.teleport('rebirth')
                    self.ui_state.teleport_buttons['Rebirth'].disbaled = False

            elif self.scene_weights[new_scene_name] < self.scene_weights[old_scene_name]:
                position = new_scene.next_gate.portal_position
                self.player.position = (position[0], position[1]+5, position[2]-3)

            new_scene.enable()
            old_scene.disable()

            print_on_screen(f'--{new_scene_name.title()}--', position=(-0.2,0.45), scale=3, duration=2)
            
            self.player.movement_locked = False
            self.ui_state.loading_hud.enabled=False


class UIState(Entity):
    def __init__(self, manager, player):
        super().__init__()
        self.manager = manager
        self.player = player
        self.damage_text = Text(parent=camera.ui, text='', position=(-0.85,-.22,0), size=0.06)
        self.armor_text = Text(parent=camera.ui, text='', position=(-0.85,-0.16), size=0.06)
        self.player_health_bar = HealthBar(max_value=20,value=20,position=(-0.85, -0.39,0),colour=color.red,scale=(0.4,0.05))
        self.player_gold_bar = HealthBar(max_value=10,value=0,position=(-0.85, -0.33,0),colour=color.gold,scale=(0.4,0.05))
        self.player_experience_bar = HealthBar(max_value=10, value=0, position=(-0.89, -0.45,0), colour=color.green, scale=(1.8, 0.05))
        self.player_gold_text = Text(parent=camera.ui, text=f'<gold>Gold', position=(-0.45, -0.34,0), scale=2)
        self.player_health_text = Text(parent=camera.ui, text=f'<red>Health', position=(-0.45, -0.4,0), scale=2)
        self.level_display = Text(parent=camera.ui, text='Level: 1', position=(-0.1, -0.35), size=0.12, font='Assets/Fonts/barber-chop/BarberChop.otf', color=color.lime)
        self.level_display.scale = 0.5
        self.teleport_text = Text(parent=camera.ui, text='Press T to open teleporter', position=(0.4, -0.4, 0), scale=1.5, color=color.red, enabled=False)
        self.reach_text = Text(parent=camera.ui, text=f'Reach: 2', position=(-0.85, -0.1, 0), size=0.04)
        self.death_screen_background = Entity(parent=camera.ui, model='quad', color=(255,0,0, 0.4), scale=(2,2), position=(0,0,-1), enabled=False)
        self.death_menu = MainMenu(None, None, bg=self.death_screen_background, header='You Died', text='Respawn', y=-0.2, enabled=False)
        #self.position_text = Text(parent=camera.ui, text=f'Position: Null', position=(-0.5, 0.5), size=0.04)
        self.crosshair = Entity(parent=camera.ui, model='quad', texture='Assets/crosshair.png', scale=0.05, position=(0,0,10))

        self.loading_hud = Entity(parent=camera.ui, position=(0,0,0), scale=2, enabled=False)
        self.loading_screen = Entity(parent=self.loading_hud, model='quad', color=color.black, scale=(10,10,1), position=(0,0,-0.1))
        self.loading_text = Text(parent=self.loading_hud, text='Loading New World...', scale=2, position=(-0.22,0.05,-0.2),color=color.white)

        self.teleport_hud = Panel(parent=camera.ui, color=color.black, enabled=False, scale=(0.7,0.6), position=(0,0,1))
        self.teleport_hud_text = Text(parent=self.teleport_hud, text='Teleport to the following', color=color.red, scale=3, origin=(0,0,0), position=(0,0.45,-1))
        self.teleport_buttons = {
            'Tutorial': Button(parent=self.teleport_hud, text='Tutorial', text_size=2, color=color.lime, scale=(0.4,0.15), position=(-0.25,0.3,-1)),
            'Market': Button(parent=self.teleport_hud, text='Market', text_size=2, color=color.lime, scale=(0.4,0.15), position=(-0.25,0.05,-1), disabled=True),
            'Centaur': Button(parent=self.teleport_hud, text='Centaur', text_size=2, color=color.lime, scale=(0.4,0.15), position=(-0.25,-0.2,-1), disabled=True),
            'Basilisk': Button(parent=self.teleport_hud, text='Basilisk', text_size=2, color=color.lime, scale=(0.4,0.15), position=(0.25,0.3,-1), disabled=True),
            'Gorgon': Button(parent=self.teleport_hud, text='Gorgon', text_size=2, color=color.lime, scale=(0.4,0.15), position=(0.25,0.05,-1), disabled=True),
            'Chimera': Button(parent=self.teleport_hud, text='Chimera', text_size=2, color=color.lime, scale=(0.4,0.15), position=(0.25,-0.2,-1), disabled=True),
            'Rebirth': Button(parent=self.teleport_hud, text='Rebirth', text_size=2, color=color.lime, scale=(0.4,0.15), position=(-0.25, -0.4, -1), disabled=False)}

    def death_screen(self):
        mouse.locked = False
        self.death_menu.enabled = True
        self.death_menu.background.enabled = True
        application.paused = True

    def update(self):
        if self.player != None:
            self.teleport_buttons['Rebirth'].on_click = lambda: self.player.teleport('rebirth')
            self.teleport_buttons['Rebirth'].disabled = False
            self.teleport_buttons['Tutorial'].on_click = lambda: self.player.teleport('tutorial')
            self.player_gold_bar.max_value = self.player.max_gold
            self.player_gold_bar.value = self.player.gold
            self.player_health_bar.max_value = self.player.max_health
            self.player_health_bar.value = round(self.player.health)
            self.player_experience_bar.max_value = self.player.levelup_req
            self.player_experience_bar.value = round(self.player.xp)
            self.damage_text.text = f'Damage: {self.player.damage}(+{self.player.damage * (self.player.weapon_level - 1)})'
            self.armor_text.text = f'Armor: {self.player.armor}'
            self.level_display.text = f'Level: {self.player.level}'
            self.reach_text.text = f'Reach: {round(self.player.basereach, 2)}'
            #self.position_text.text = f'Position: {self.player.position}'

            if self.player.health <= 0 and not self.death_menu.enabled:
                if self.death_menu.start_function is None:
                    self.death_menu.start_function = self.player.death
                self.death_screen()
                self.teleport_hud.enabled=False

    def input(self, key):
        if key == 't' and not self.manager.store.enabled and (self.player.can_teleport or self.manager.debug_mode):
            self.teleport_hud.enabled = not self.teleport_hud.enabled
            self.player.movement_locked = self.teleport_hud.enabled
            mouse.locked = not self.teleport_hud.enabled
            self.teleport_text.enabled = False


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
            self.world = GorgonMap(manager, parent=self)
            self.boss_type = 'fbx'
        elif self.name == 'Chimera':
            self.world = ChimeraMap(manager, parent=self)
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
    if key == 'tab' and main_menu.started and manager.debug_mode:
        spectator_mode.enabled = not spectator_mode.enabled
        spectator_mode.position = manager.player.position
        application.paused = spectator_mode.enabled
        camera.parent = spectator_mode if spectator_mode.enabled else manager.player

#------------------------------------------------------------#

app = Ursina()

window.icon = 'Assets/ursina.ico'
window.exit_button.visible = False
#window.editor_ui.enabled = False
spectator_mode = EditorCamera(enabled = False, ignore_paused=True)
pause_handler = Entity(ignore_paused=True, input=spectator_input)
manager = GameManager()
main_menu = MainMenu(manager.start_game, manager.resume_game)

def input(key):
    if key == 'c':
        manager.debug_mode = not manager.debug_mode
    if key == 'l':
        manager.player.position=(0,1,0)

def update():
    if held_keys['escape']:
        manager.pause_game()
    if manager.player is not None and manager.debug_mode:
        if held_keys['g']:
            manager.player.gold += 1000
        if held_keys['x']:
            manager.player.xp += 100

app.run()
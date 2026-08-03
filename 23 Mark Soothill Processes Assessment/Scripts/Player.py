"""The player class used to create and handle the player of the dungeon game."""
from ursina import Entity, color, application, Vec3, time, held_keys, curve, invoke, raycast, scene, camera, mouse

class Player(Entity):
    """."""
    def __init__(self, ui_state, manager):
        """."""
        # Create a body to represent the player
        super().__init__(model='cube', scale=(1,2.5,1), position=(0,1,0),
                         collider='box', visible_self=manager.debug_mode,
                         color=color.orange)

        # Intialize the passed-in main classes
        self.ui_state = ui_state
        self.manager = manager

        # Intialize the player stats
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
        self.old_req = 3
        self.levelup_req = 5
        self.xp = 0
        self.xp_multi = 1
        self.gold = 0
        self.max_gold = 10
        self.gold_multi = 1
        self.inventory = None
        self.weapon_level = 1
        self.basereach = 3
        self.distance = float('inf')
        self.movement_locked = False
        self.store = None
        self.at_stall = False
        self.regeneration_value = 0
        self.can_teleport = False
        self.gorgon_protection = False
        self.lava_protection = False
        self.is_dead = False
        
        camera.position = (0,1,0)
        camera.rotation = (0,0,0)
        camera.parent = self
        camera.fov = 100
        mouse.locked = True

        self.hand = Entity(model='Assets/Models/Hands/handv5.fbx',texture='Assets/Models/Hands/skin.jpg',
                            parent=self, scale=0.05, collider='box',position=(1,0.5, -1), rotation=(1,1,-25), double_sided = True)
        self.store_icon = Entity(parent=camera.ui, model='quad', texture='Assets/Store Icon.png', position=(0,0,5), scale=(0.4,0.1), alpha=0)

        self.manager.ignore_list.append(self)
        self.manager.ignore_list.append(self.hand)

    def death(self):
        print(2)
        self.is_dead = False
        application.paused = False
        self.position = Vec3(0,10,0)
        self.max_health = self.max_health - self.level * 2 if self.max_health - self.level*2 >= 20 else self.max_health
        self.health = self.max_health
        self.gold = self.gold // 2
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
            self.manager.switch_scenes(scenes)
    
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
        self.damage += 1
        self.armor += 0.25
        self.basereach += 0.1
    
    def teleport(self, location):
        self.at_stall = False
        self.store_icon.alpha = 0
        self.manager.switch_scenes(f'{self.manager.location}.{location}')
    
    def punch(self):
        self.hand.animate_position((1,1,1), duration=0.1, curve=curve.in_out_sine)
        invoke(self.unpunch, delay=0.1)
    def unpunch(self):
        self.hand.animate_position((1,0.5,-1), duration=0.1, curve=curve.in_out_sine)

    def update(self):
        """."""
        if round(self.xp) >= round(self.levelup_req):
            self.levelup()

        self.check_max_gold()
        self.check_max_health()
        
        self.health += self.regeneration_value * time.dt

        # Allow jumping only when the player is on the ground
        ground_ray = raycast(self.position + Vec3(0,0.5,0), direction=Vec3(0,-1,0), distance=2, ignore=self.manager.ignore_list, debug=self.manager.debug_mode)
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
            self.speed = self.default_speed * 1.5
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
        markets = {'market': self.manager.market_world,
                   'rebirth': self.manager.rebirth_world}

        if self.manager.location in markets:
            colliders = markets[self.manager.location].colliders
            for collider in colliders:
                if self.intersects(collider).hit and mouse.hovered_entity.name.lower() in markets:
                    collider.color = color.red
                    self.store = collider.name
                    self.store_icon.alpha = 1
                    self.at_stall = True
                            
                else:
                    collider.color = color.white
                    self.store = None
                    self.store_icon.alpha = 0
                    self.at_stall = False

        # Check if nothing is infront of the player before moving
        hit_info = raycast(self.world_position, movement, distance=0.5, debug=self.manager.debug_mode, ignore=self.manager.ignore_list)
        if not hit_info.hit:
            if not self.movement_locked or self.is_dead:
                move_amount = movement * self.speed * time.dt
                self.position += move_amount
        else:
            name = hit_info.entity.name
            if name.startswith('gate') and name.split('.')[-1] == 'complete':
                scenes = name[5:]
                delay = 0.01
                if self.manager.scenes[scenes.split('.')[1]] == None:
                    self.manager.ui_state.loading_hud.enabled = True
                    delay = 0.05
                invoke(lambda: self.manager.switch_scenes(scenes), delay=delay)

    def input(self, key):
        if key == 'e' and self.at_stall and not self.ui_state.teleport_hud.enabled:
            if self.store == 'Market':
                self.manager.store.enabled = not self.manager.store.enabled
            elif self.store == 'Rebirth':
                self.manager.rebirth_store.enabled = not self.manager.rebirth_store.enabled

            self.movement_locked = not self.movement_locked
            mouse.locked = not mouse.locked
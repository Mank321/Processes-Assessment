from ursina import Entity, color, application, Vec3, time, held_keys, curve, invoke, raycast, camera, mouse

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
        self.damage = 1
        self.level = 1
        self.old_req = 3
        self.levelup_req = 5
        self.xp = 0
        self.xp_multi = 1
        self.stamina = 5
        self.max_stamina = self.stamina
        self.gold = 0
        self.max_gold = 10
        self.inventory = None
        self.weapon_level = 0
        self.basereach = 2
        self.distance = float('inf')
        self.movement_locked = False
        self.gorgon_protection = False
        self.lava_protection
        
        camera.position = (0,1,0)
        camera.rotation = (0,0,0)
        camera.parent = self
        camera.fov = 100
        mouse.locked = True

        self.hand = Entity(model='Assets/Models/Hands/handv5.fbx',texture='Assets/Models/Hands/skin.jpg',
                            parent=self, scale=0.05, collider='box',position=(1,0.5, -1), rotation=(1,1,-25), double_sided = True)
        self.store_icon = Entity(parent=camera.ui, model='quad', texture='Assets/Store Icon.png', position=(0,0,10), scale=(0.4,0.1), alpha=0)

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
        self.max_stamina += 2
        self.damage += 1
        self.armor += 0.25
        self.basereach += 0.1
    
    def teleport(self, location):
        self.manager.switch_scenes(f'{self.manager.location}.{location}')
    
    def punch(self):
        self.hand.animate_position((1,1,1), duration=0.1, curve=curve.in_out_sine)
        invoke(self.unpunch, delay=0.1)
    def unpunch(self):
        self.hand.animate_position((1,0.5,-1), duration=0.1, curve=curve.in_out_sine)

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
        dictionary = {'tutorial': self.manager.tutorial_world,
                      'market': self.manager.market_world,
                      'centaur': self.manager.centaur_world,
                      'basilisk': self.manager.basilisk_world,
                      'gorgon': self.manager.gorgon_world,
                      'chimera': self.manager.chimera_world}

        colliders = dictionary[self.manager.location].colliders
        for collider in colliders:
            if self.intersects(collider).hit:
                collider.color = color.red
                if collider.name == 'stall':
                    self.store_icon.alpha = 1
                    self.at_stall = True
                        
            else:
                collider.color = color.white
                if collider.name == 'stall':
                    self.store_icon.alpha = 0
                    self.at_stall = False
        
        # Check if nothing is infront of the player before moving
        ignore = [self, self.hand]
        hit_info = raycast(self.world_position, movement, distance=0.5, debug=self.manager.debug_mode, ignore=ignore)
        if not hit_info.hit:
            if not self.movement_locked:
                move_amount = movement * self.speed * time.dt
                self.position += move_amount
        else:
            name = hit_info.entity.name
            if name.startswith('gate') and name.split('.')[-1] == 'complete':
                scenes = name[5:]
                self.manager.switch_scenes(scenes)
    def input(self, key):
        if key == 'e' and self.at_stall:
            self.manager.store.enabled = not self.manager.store.enabled
            self.movement_locked = not self.movement_locked
            mouse.locked = not mouse.locked
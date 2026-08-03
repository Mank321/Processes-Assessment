from ursina import Entity, Vec3, color, time, curve, invoke, distance, print_on_screen, camera, mouse
from ursina.shaders import unlit_shader

class Monster(Entity):
    def __init__(self, manager, parent, monster_stats, is_boss=False, is_tutorial=False, gate=None, position=Vec3(0,0,0), rotation=Vec3(0,180,0), scale=1, enabled=True):
        super().__init__(model=f'Assets/Models/{monster_stats["name"]}/base_monsterV2.fbx',
                       texture=f'Assets/Models/{monster_stats["name"]}/texture.png',
                       position=position, double_sided=True, scale=monster_stats['scale']*scale,
                       rotation=rotation, name=monster_stats["name"], parent=parent, enabled=enabled,
                       shader=unlit_shader, cache_compiled_model=False, collider='box', on_click=lambda: self.onClick())

        self.manager = manager
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
        self.scale = monster_stats['scale']
        self.position = position
        self.origin_position = position
        self.rotation = rotation
        self.origin_rotation = rotation
        self.is_boss = is_boss
        self.is_boss_true = is_boss
        self.is_tutorial = is_tutorial
        self.gate = gate
        boss = 'bosss'
        if self.name == 'Basilisk':
            boss = 'bossV5'
        

        if self.is_boss:
            self.model = f'Assets/Models/{self.name}/Boss/{boss}.fbx'
            self.texture = f'Assets/Models/{self.name}/Boss/texture.png'
            self.scale = monster_stats['boss_scale']
            self.speed = monster_stats['boss_speed']
            self.closeness = monster_stats['boss_closeness']
            self.sight = monster_stats['boss_sight']
            #self.boss_rotation = monster_stats['boss_rotation']
            self.collider = 'box'
            #self.origin_rotation = self.boss_rotation
            self.damage *= 5
            self.health *= 10
            self.max_health = self.health
            self.worth *= 10

        if self.is_boss or self.is_tutorial:
            self.manager.portal_monsters.append(self)

        #self.collider.visible = True
        self.manager.ignore_list.append(self)

    def death(self):
        self.visible = False
        self.enabled = False
        self.ignore = True
        self.is_boss = False
        self.is_tutorial = False
        invoke(self.respawn, delay=self.monster_delay)
    
    def respawn(self):
        self.position = self.origin_position
        self.rotation = self.origin_rotation
        self.visible = True
        self.enabled = True
        self.ignore = False
        self.health = self.max_health

    def onClick(self):
        """This triggers when the mouse clicks the monster."""
        self.distance = distance(self, self.manager.player)
        if self.distance <= self.manager.player.basereach + self.closeness and not self.manager.player.is_dead:
            self.health -= self.manager.player.damage * self.manager.player.weapon_level
            self.manager.player.punch()

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
                self.manager.player.gold += self.worth * self.manager.player.gold_multi
                self.manager.ui_state.player_gold_bar.value += self.worth
                self.manager.player.xp += self.worth * 2 * self.manager.player.xp_multi
                self.manager.ui_state.player_experience_bar.value += self.worth
                self.death()

    def update(self):
        """."""
        self.distance = distance(self, self.manager.player)
        if self.closeness < self.distance <= self.sight and not self.manager.player.is_dead:
            self.look_at_2d(self.manager.player, 'y')
            self.position += self.forward * time.dt * self.speed
            if self.name == 'Gorgon' and not self.manager.player.gorgon_protection:
                self.manager.player.health -= 100 * time.dt

        if self.distance <= self.closeness and not self.manager.player.is_dead:
            damage_delt = self.damage - self.manager.player.armor
            if damage_delt >= 0:
                self.manager.player.health -= damage_delt * time.dt * self.attack_speed

    def input(self, key):
        if (key == 'left mouse up' or key == 'right mouse up') and mouse.hovered_entity == self:
            self.onClick()
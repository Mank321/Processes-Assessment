from ursina import Entity, color, Text, Button, Tooltip, Ursina, camera

#Make an upgrades class and create an object for each upgrade
class Store(Entity):
    def __init__(self, manager, enabled=False):
        super().__init__(parent=camera.ui, model='quad', color=color.black, position=(0.1,0.1,0), scale=(0.9, 0.7, 1), enabled=enabled)

        self.manager = manager
        self.player_hud = Entity(parent=self, enabled=True)
        self.shop_hud = Entity(parent=self, enabled=False)
        self.skill_hud = Entity(parent=self, enabled=False)

        self.player_button = Button(parent=self, color=color.gray, scale=(0.17, 0.20), position=(-0.5, 0.37,-1), icon='Profile Icon.png', tooltip=Tooltip(f'<green>Player Stats'),
                                    on_click=lambda: self.switch(self.player_hud, self.shop_hud, self.skill_hud))
        self.shop_button = Button(parent=self, color=color.gray, scale=(0.17,0.20), position=(-0.5, 0,-1), icon='store.png', tooltip=Tooltip(f'<green>Shop'),
                                  on_click=lambda: self.switch(self.shop_hud, self.player_hud, self.skill_hud))
        self.skill_button = Button(parent=self, color=color.gray, scale=(0.17,0.2), position=(-0.5, -0.37,-1), icon='fireball skill icon.jpg', tooltip=Tooltip(f'<green>Skills'),
                                   on_click=lambda: self.switch(self.skill_hud, self.player_hud, self.shop_hud))

        self.health_upgrade_cost = 5
        self.damage_upgrade_cost = 5
        self.speed_upgrade_cost = 5
        self.experience_upgrade_cost = 15
        self.reach_upgrade_cost = 5

        self.bag_upgrade_cost = 10
        self.armor_upgrade_cost = 15
        self.weapon_upgrade_cost = 50

        self.regeneration_upgrade_cost = 10
        self.teleport_cost = 50
        self.gorgon_gaze_cost = 400
        self.lava_protection_cost = 1500

        self.health_text = Text(parent=self.player_hud, text=f'Health Increase Cost: {self.health_upgrade_cost}', position=(-0.4,0.4,-1))
        self.health_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0.2,0.4,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Health'))
        self.damage_text = Text(parent=self.player_hud, text=f'Damage Increase Cost: {self.damage_upgrade_cost}', position=(-0.4,0.28,-1))
        self.damage_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0.2,0.28,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Damage'))
        self.speed_text = Text(parent=self.player_hud, text=f'Speed Increase Cost: {self.speed_upgrade_cost}', position=(-0.4,0.16,-1))
        self.speed_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0.2,0.16,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Speed'))
        self.experience_text = Text(parent=self.player_hud, text=f'Experience Multiplier Cost: {self.experience_upgrade_cost}', position=(-0.4,0.04,-1))
        self.experience_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0.2,0.04,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Experience'))
        self.reach_text = Text(parent=self.player_hud, text=f'Reach Increase Cost: {self.reach_upgrade_cost}', position=(-0.4,-0.08,-1))
        self.reach_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0.2,-0.08,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Reach'))

        self.bag_text = Text(parent=self.shop_hud, text=f'Gold Bag Multiplier Cost: {self.bag_upgrade_cost}', position=(-0.4,0.4,-1))
        self.bag_button = Button(parent=self.shop_hud, color=color.lime, text='Buy', position=(0.2,0.4,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Gold Bag'))
        self.armor_text = Text(parent=self.shop_hud, text=f'Armor Increase Cost: {self.armor_upgrade_cost}', position=(-0.4,0.28,-1))
        self.armor_button = Button(parent=self.shop_hud, color=color.lime, text='Buy', position=(0.2,0.28,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Armor'))
        self.weapon_text = Text(parent=self.shop_hud, text=f'Weapon Level Cost (W.I.P): {self.weapon_upgrade_cost}', position=(-0.4,0.16,-1))
        self.weapon_button = Button(parent=self.shop_hud, color=color.lime, text='Buy', position=(0.2,0.16,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Weapon'))

        self.regeneration_text = Text(parent=self.skill_hud, text=f'Regeneration Increase Cost: {self.regeneration_upgrade_cost}', position=(-0.4,0.4,-1))
        self.regeneration_button = Button(parent=self.skill_hud, color=color.lime, text='Buy', position=(0.2,0.4,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Regeneration'))
        self.teleportation_text = Text(parent=self.skill_hud, text=f'Teleportation Skill Cost: {self.teleport_cost}', position=(-0.4,0.28,-1))
        self.teleportation_button = Button(parent=self.skill_hud, color=color.lime, text='Buy', position=(0.2,0.28,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Teleport'))
        self.gorgon_gaze_text = Text(parent=self.skill_hud, text=f'Gorgon Protection Skill Cost: {self.gorgon_gaze_cost}', position=(-0.4,0.16,-1))
        self.gorgon_gaze_button = Button(parent=self.skill_hud, color=color.lime, text='Buy', position=(0.2,0.16,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Gorgon Gaze'))
        self.lava_protection_text = Text(parent=self.skill_hud, text=f'Lava Protection Skill Cost: {self.lava_protection_cost}', position=(-0.4,0.04,-1))
        self.lava_protection_button = Button(parent=self.skill_hud, color=color.lime, text='Buy', position=(0.2,0.04,-1), scale=(0.1,0.1), on_click=lambda: self.buy('Lava Protection'))

        self.help_text = Entity(parent=self, model='quad', texture='Assets/store help text.png', position=(-0.8,-0.2,-2), scale=(0.5,0.5,0.5))
        self.exit_text = Text(parent=self, text='Press E to exit', color=color.white, position=(0.2, -0.4,-1))

    def switch(self, new, old1, old2):
        new.enable()
        old1.disable()
        old2.disable()

    def buy(self, stat):
        costs = {'Health': self.health_upgrade_cost,
                 'Damage': self.damage_upgrade_cost,
                 'Speed': self.speed_upgrade_cost,
                 'Experience': self.experience_upgrade_cost,
                 'Reach': self.reach_upgrade_cost,
                 'Gold Bag': self.bag_upgrade_cost,
                 'Armor': self.armor_upgrade_cost,
                 'Weapon': self.weapon_upgrade_cost,
                 'Regeneration': self.regeneration_upgrade_cost,
                 'Teleport': self.teleport_cost,
                 'Gorgon Gaze': self.gorgon_gaze_cost,
                 'Lava Protection': self.lava_protection_cost}

        if self.manager.player.gold >= costs[stat]:
            if stat == 'Health':
                self.manager.player.max_health += 5
                self.manager.player.health += 5
                self.health_upgrade_cost *= 1.2
                self.health_upgrade_cost = round(self.health_upgrade_cost)
                self.health_text.text = f'{stat} Increase Cost: {self.health_upgrade_cost}'
            elif stat == 'Damage':
                self.manager.player.damage += 1
                self.damage_upgrade_cost *= 1.7
                self.damage_upgrade_cost = round(self.damage_upgrade_cost)
                self.damage_text.text = f'{stat} Increase Cost: {self.damage_upgrade_cost}'
            elif stat == 'Speed':
                self.manager.player.speed += 2
                self.speed_upgrade_cost *= 2
                self.speed_upgrade_cost = round(self.speed_upgrade_cost)
                self.speed_text.text = f'{stat} Increase Cost: {self.speed_upgrade_cost}'
            elif stat == 'Experience':
                self.manager.player.xp_multi *= 1.2
                self.experience_upgrade_cost *= 1.6
                self.experience_upgrade_cost = round(self.experience_upgrade_cost)
                self.experience_text.text = f'{stat} Multiplier Cost: {self.experience_upgrade_cost}'
            elif stat == 'Reach':
                self.manager.player.basereach += 0.25
                self.reach_upgrade_cost *= 1.4
                self.reach_upgrade_cost = round(self.reach_upgrade_cost)
                self.reach_text.text = f'{stat} Increase Cost: {self.reach_upgrade_cost}'
            elif stat == 'Gold Bag':
                self.manager.player.max_gold *= 2
                self.bag_upgrade_cost *= 2
                self.bag_upgrade_cost = round(self.bag_upgrade_cost)
                self.bag_text.text = f'{stat} Multiplier Cost: {self.bag_upgrade_cost}'
            elif stat == 'Armor':
                self.manager.player.armor += 0.25
                self.armor_upgrade_cost *= 2
                self.armor_upgrade_cost = round(self.armor_upgrade_cost)
                self.armor_text.text = f'{stat} Increase Cost: {self.armor_upgrade_cost}'
            elif stat == 'Weapon':
                self.manager.player.weapon_level *= 2
                self.weapon_upgrade_cost *= 3
                self.weapon_upgrade_cost = round(self.weapon_upgrade_cost)
                self.weapon_text.text = f'{stat} Level Cost (W.I.P): {self.weapon_upgrade_cost}'
            elif stat == 'Regeneration':
                self.manager.player.regeneration_value += self.manager.player.max_health * 0.01
                self.regeneration_upgrade_cost *= 5
                self.regeneration_upgrade_cost = round(self.regeneration_upgrade_cost)
                self.regeneration_text.text = f'{stat} Increase Cost: {self.regeneration_upgrade_cost}'
            elif stat == 'Teleport':
                self.manager.player.can_teleport = True
                self.teleportation_text.text = f'{stat} Skill Cost: Bought'
                self.teleportation_button.disable()
                self.manager.ui_state.teleport_text.enabled=True
            elif stat == 'Gorgon Gaze':
                self.manager.player.gorgon_protection = True
                self.gorgon_gaze_text.text = f'{stat} Skill Cost: Bought'
                self.gorgon_gaze_button.disable()
            elif stat == 'Lava Protection':
                self.manager.player.lava_protection = True
                self.lava_protection_text.text = f'{stat} Skill Cost: Bought'
                self.lava_protection_button.disable()


            self.manager.player.gold -= costs[stat]

if __name__ == '__main__':
    app=Ursina()

    class Player():
        def __init__(self):
            self.gold = 0
            self.max_gold = 10
            self.health = 20
            self.damage = 1
            self.speed = 50
            self.xp_multi = 1
            self.basereach = 2
            self.max_gold = 10
            self.armor = 0
            self.weapon_level = 0
    class Manager():
        def __init__(self):
            self.player = Player()


    manager = Manager()

    store = Store(manager)

    def input(key):
        if key =='e':
            store.enabled = not store.enabled
        if key == 'm':
            manager.player.gold += 10
        if key =='s':
            print(f'Gold {manager.player.gold}')
            print(f'Health {manager.player.health}')
            print(f'Damage {manager.player.damage}')
            print(store.damage_upgrade_cost)
            print(f'Speed {manager.player.speed}')
            print(f'Experience {manager.player.xp_multi}')
            print(f'Reach {manager.player.basereach}')
            print(f'Bag {manager.player.max_gold}')
            print(f'Armor {manager.player.armor}')
            print(f'Weapon {manager.player.weapon_level}')

    app.run()
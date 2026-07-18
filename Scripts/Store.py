from ursina import Entity, color, Text, Button, Tooltip, Ursina, camera

class Store(Entity):
    def __init__(self, manager, enabled=False):
        super().__init__(parent=camera.ui, model='quad', color=color.black, position=(0,0,0), scale=(0.9, 0.7, 1), enabled=enabled)

        self.manager = manager
        self.player_hud = Entity(parent=self, enabled=True)
        self.shop_hud = Entity(parent=self, enabled=False)

        self.player_button = Button(parent=self, color=color.gray, scale=(0.17, 0.20), position=(-0.5, 0.37), icon='Profile Icon.png', tooltip=Tooltip(f'<green>Player Stats'),
                                    on_click=lambda: setattr(self.player_hud, 'enabled', not self.player_hud.enabled))
        self.shop_button = Button(parent=self, color=color.gray, scale=(0.17,0.20), position=(-0.5, 0), icon='store.png', tooltip=Tooltip(f'<green>Shop'),
                                  on_click=lambda: setattr(self.shop_hud, 'enabled', not self.shop_hud.enabled))

        self.health_upgrade_cost = 5
        self.health_upgrade_markup = 1.5
        self.damage_upgrade_cost = 5
        self.damage_upgrade_markup = 2
        self.speed_upgrade_cost = 5
        self.speed_upgrade_markup = 2
        self.experience_upgrade_cost = 15
        self.experience_upgrade_markup = 1.5
        self.reach_upgrade_cost = 5
        self.reach_upgrade_markup = 1.5
        self.bag_upgrade_cost = 10
        self.bag_upgrade_markup = 2
        self.armor_upgrade_cost = 15
        self.armor_upgrade_markup = 3
        self.weapon_upgrade_cost = 15
        self.weapon_upgrade_markup = 5

        self.health_text = Text(parent=self.player_hud, text=f'Health Increase Cost: {self.health_upgrade_cost}', position=(-0.4,0.4))
        self.health_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0,0.4), scale=(0.1,0.1), on_click=lambda: self.buy('Health'))
        self.damage_text = Text(parent=self.player_hud, text=f'Damage Increase Cost: {self.damage_upgrade_cost}', position=(-0.4,0.28))
        self.damage_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0,0.28), scale=(0.1,0.1), on_click=lambda: self.buy('Damage'))
        self.speed_text = Text(parent=self.player_hud, text=f'Speed Increase Cost: {self.speed_upgrade_cost}', position=(-0.4,0.16))
        self.speed_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0,0.16), scale=(0.1,0.1), on_click=lambda: self.buy('Speed'))
        self.experience_text = Text(parent=self.player_hud, text=f'Experience Multiplier Cost: {self.experience_upgrade_cost}', position=(-0.4,0.04))
        self.experience_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0,0.04), scale=(0.1,0.1), on_click=lambda: self.buy('Experience'))
        self.reach_text = Text(parent=self.player_hud, text=f'Reach Increase Cost: {self.reach_upgrade_cost}', position=(-0.4,-0.08))
        self.reach_button = Button(parent=self.player_hud, color=color.lime, text='Buy', position=(0,-0.08), scale=(0.1,0.1), on_click=lambda: self.buy('Reach'))
        self.bag_text = Text(parent=self.shop_hud, text=f'Bag Multiplier Cost: {self.bag_upgrade_cost}', position=(-0.4,-0.2))
        self.bag_button = Button(parent=self.shop_hud, color=color.lime, text='Buy', position=(0,-0.2), scale=(0.1,0.1), on_click=lambda: self.buy('Bag'))
        self.armor_text = Text(parent=self.shop_hud, text=f'Armor Increase Cost: {self.armor_upgrade_cost}', position=(-0.4,-0.32))
        self.armor_button = Button(parent=self.shop_hud, color=color.lime, text='Buy', position=(0,-0.32), scale=(0.1,0.1), on_click=lambda: self.buy('Armor'))
        self.weapon_text = Text(parent=self.shop_hud, text=f'Weapon Level Cost: {self.weapon_upgrade_cost}', position=(-0.4,-0.44))
        self.weapon_button = Button(parent=self.shop_hud, color=color.lime, text='Buy', position=(0,-0.44), scale=(0.1,0.1), on_click=lambda: self.buy('Weapon'))


    def buy(self, stat):
        stats = {'Health': [self.health_upgrade_cost, 'add', 5, self.health_upgrade_markup, self.manager.player.health, self.health_text],
                 'Damage': [self.damage_upgrade_cost, 'add', 1, self.damage_upgrade_markup, self.manager.player.damage, self.damage_text],
                 'Speed': [self.speed_upgrade_cost, 'add', 2, self.speed_upgrade_markup, self.manager.player.speed, self.speed_text],
                 'Experience': [self.experience_upgrade_cost, 'multi', 1.2, self.experience_upgrade_markup, self.manager.player.xp_multi, self.experience_text],
                 'Reach': [self.reach_upgrade_cost, 'add', 0.5, self.reach_upgrade_markup, self.manager.player.basereach, self.reach_text],
                 'Bag': [self.bag_upgrade_cost, 'multi', 2, self.bag_upgrade_markup, self.manager.player.max_gold, self.bag_text],
                 'Armor': [self.armor_upgrade_cost, 'add', 0.25, self.armor_upgrade_markup, self.manager.player.armor, self.armor_text],
                 'Weapon': [self.weapon_upgrade_cost, 'add', 1, self.weapon_upgrade_markup, self.manager.player.weapon_level, self.weapon_text]}
        if self.manager.player.gold >= stats[stat][0]:
            if stats[stat][1] == 'add':
                stats[stat][4] += stats[stat][2]
            else:
                stats[stat][4] *= stats[stat][2]
            self.manager.player.gold -= stats[stat][0]
            stats[stat][0] *= stats[stat][3]
            stats[stat][5].text = f'{stat} Cost: {stats[stat][0]}'
            print(self.manager.player.damage)

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
            self.bag = 10
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

    app.run()
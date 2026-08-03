# imports
# constants
# functions
# name
# tutorial
# playing_game
#   variables
#   game loop
#     reincanate variables
#     monster loop
#     monster stats
#     facing monster
#     reincarnate
#     levelup
#       skills
#       hecate
#     bonuses
#     bosses
#     reincarnate
#     ares
#   shop
#     bag
#     armor
#     rations
#  go home
# dead

# Ideas:
# incounter with gods(done: hades, ares, hecate To Do: Zeus(all bosses killed))
# quests
# monster grade (epic, common, legendary) can altar strength and treasure
# stats screen
# classes(mages, knights, ect)

import time
import random
from colorama import Fore

# Making sure health doesnt go over max health


def increasehealth(health, max_health):
    if health > max_health:
        health = max_health
    return health


# Turning the regain health into a variable


def regainhealth(regain_health, health, regain_health_rate):
    if regain_health is True:
        health += regain_health_rate

    return health


# Creating a funtion that will run whenever the player dies


def dead(health, dead_by_boss, play_again, monsters_killed,  max_health,
         boss_monsters_killed, round_number, playing_game, hades_temp_true,
         hades, total_rounds):
    if health <= 0:
        if dead_by_boss is False:
            print("The monsters have dealt a fatal blow and killed you")
        else:
            dead_by_boss = False
        while play_again not in yes_or_no:
            time.sleep(TIME_SLEEP)
            play_again = input(f"{Fore.GREEN}Do you want to reincarnate? ")

# If the player wants to play again but didnt kill many monsters
        if play_again == "yes" and monsters_killed <= GODS_DISSAPOINTED:
            print("Though the gods are dissapointed in you, they will "
                  "grant you another life")
            time.sleep(TIME_SLEEP)
            print(f"You shall be reincarnated in {area}")
            health = max_health
            round_number = 1
            hades_temp_true = True

# If the player wants to play again and they killed many monsters
        elif play_again == "yes" and monsters_killed >= GODS_PLEASED\
                and boss_monsters_killed <= NOT_ENOUGH_BOSSES:
            print("You have pleased the gods!")
            time.sleep(TIME_SLEEP)
            print("You shall now be granted a new life")
            health = max_health
            round_number = 1
            hades_temp_true = True

# If the player wants to play again and they killed many monsters and boss
# monsters
        elif play_again == "yes" and boss_monsters_killed >= ENOUGH_BOSSES\
                and hades is False:
            time.sleep(TIME_SLEEP)
            print("You have gained the favour of Hades, Lord of the Dead!")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.BLACK}Hades: Greetings {name}! I am Hades! Lord of "
                  "the Dead")
            time.sleep(TIME_SLEEP)
            print("Hades: I have bestowed apon you my blessing as a "
                  "reward for having killed 5 or more bosses before "
                  "your death!")
            time.sleep(TIME_SLEEP)
            print("Hades: My blessing will grant you +30 Max Health and "
                  "+10 Armor!")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.GREEN}{name}: Thank you Lord Hades, for your "
                  "gift, I will treasure it well")
            print(f"{Fore.BLACK}Hades: And so you shall. Now be off with "
                  "you!")
            health = max_health
            hades = True
            hades_temp_true = True
            round_number = 1

# If the player has already met hades and died again
        elif play_again == "yes" and hades is True:
            print("Hades: Come on hero! Get back up there")
            hades_temp_true = True
            health = max_health

        elif play_again == "no":
            playing_game = ""
            round_number = total_rounds * total_rounds

    death_output_variables.append(health)
    death_output_variables.append(dead_by_boss)
    death_output_variables.append(play_again)
    death_output_variables.append(round_number)
    death_output_variables.append(playing_game)
    death_output_variables.append(hades_temp_true)
    death_output_variables.append(hades)

    return death_output_variables


# Stating the constant variables
TIME_SLEEP = 1
TUTORIAL_SLEEP = 5
STARTING_MONSTER_TREASURE = 5
GODS_DISSAPOINTED = 9
GODS_PLEASED = 10
NOT_ENOUGH_BOSSES = 1
ENOUGH_BOSSES = 2
STARTING_ROUNDS = 5
SKILL_CHANCE = 10
CYCLOPS_HEALTH = 100
GORGON_HEALTH = 200
CHIMERA_HEALTH = 300
GIANT_HEALTH = 400
TYPHON_HEALTH = 500
CYCLOPS_DAMAGE = 15
GORGON_DAMAGE = 25
CHIMERA_DAMAGE = 35
GIANT_DAMAGE = 45
TYPHON_DAMAGE = 55
CYCLOPS_SKILL = "Club Smash"
GORGON_SKILL = "Petrification"
CHIMERA_SKILL = "Fire Breath"
GIANT_SKILL = "Stomp"
TYPHON_SKILL = "Scream"
CYCLOPS_SKILL_DAMAGE = 20
GORGON_SKILL_DAMAGE = 9999
CHIMERA_SKILL_DAMAGE = 40
GIANT_SKILL_DAMAGE = 50
TYPHON_SKILL_DAMAGE = 60
FIRE_BALL_SKILL_COST = 10
FIRE_BALL_SKILL_DAMAGE = 10
FIRE_BALL_SKILL_USES = 10
FORCE_FIELD_SKILL_COST = 50
FORCE_FIELD_SKILL_USES = 2
HEAL_SKILL_COST = 10
HEAL_SKILL_HEALING = 10
HEAL_SKILL_USES = 3
METEOR_SKILL_COST = 25
METEOR_SKILL_DAMAGE = 30
METEOR_SKILL_USES = 4
MANA_REGENERATION_SKILL_COST = 10
MANA_REGENERATION_SKILL_EFFECT = 50
MANA_REGENERATION_SKILL_USES = 3
SPATIAL_SLASH_SKILL_COST = 50
SPATIAL_SLASH_SKILL_DAMAGE = 50
SPATIAL_SLASH_SKILL_USES = 2
FINAL_ASSAULT_SKILL_DAMAGE = 5
CYCLOPS_KILLS_NEEDED = 5
GORGON_KILLS_NEEDED = 5
WILD_CENTAUR_KILLS_NEEDED = 5
GIANT_KILLS_NEEDED = 5
BASILISK_KILLS_NEEDED = 5


# Asking the player for their name
name = ""
while name == "":
    name = input(f"{Fore.GREEN}Good morning Greek adventurer! Whats your "
                 "name? ").strip()
    name_length = len(name)

    if name == "":
        print("Come on, atleast type something")

    if name_length > 10:
        print("That name is too long")
        name = ""
    time.sleep(TIME_SLEEP)

print(f"Nice to meet you {name}")
time.sleep(TIME_SLEEP)


# Asking the playing if they'd like to read a tutorial
yes_or_no = ["yes", "no"]
tutorial = ""
while tutorial not in yes_or_no:
    tutorial = input("Would you like a tutorial? Please answer with either "
                     "yes or no. ").lower().strip()
    time.sleep(TIME_SLEEP)
    if tutorial not in yes_or_no:
        print(f"That's not what I asked for {name}")
        time.sleep(TIME_SLEEP)


# Displaying the tutorial
if tutorial == "yes":
    print(f"\n{'>' * 20} Tutorial {'<' * 20}")
    print("\nYou are an adverturer, it is your job to hunt down monsters.")
    time.sleep(TIME_SLEEP)

    print("\nHealth: Health is rather self explanitory, It is how much damage"
          " you can take from monsters, and if your health reaches 0, you will"
          " die. You can get health from bonuses, leveling up, and getting"
          " rewarded by gods")
    time.sleep(TUTORIAL_SLEEP)

    print("\nArmor: Armor is also rather self explanitory. For each point of"
          " armor, you take 1 point less of damage. The more armor you have,"
          " the stronger the monsters you can fight.\nArmor can be obtained"
          " from bonuses, leveling up, and from the shop.")
    time.sleep(TUTORIAL_SLEEP)

    print("\nTreasure: Treasure is basically money. It is used in the shop"
          " when you want to buy items.\nTreasure can be gained from monsters,"
          " one of the two stats that they have, apart from attack, is how"
          " much treasure they drop.\nTreasure Luck is a bonus you can get"
          " that increases the amount of treasure you can get from monsters."
          "\nBut be careful, you can't get more treasure than you can carry in"
          " your bag, or you'll be forced to leave it behind.")
    time.sleep(TUTORIAL_SLEEP)

    print("\nShop: The shop can be reached whenever you finished you hunt for"
          " killing monsters. The shop will allow you to buy items like a"
          " bigger bag, so you can carry more treasure on your journeys."
          "\nArmor so you can get stronger and stronger.\nAnd rations,"
          " allowing you to fight more monsters over longer periods of time."
          "\nDon't forget that each time you buy something, the price for"
          " it increases!")
    time.sleep(TUTORIAL_SLEEP)

    print("\nBonuses: Bonuses are sometimes found after killing monsters."
          "\nThey could be getting higher max health, getting more health or"
          " armor, more rations for exploring, and so much more.")
    time.sleep(TUTORIAL_SLEEP)

    print("\nLevels: Levels are one of the main points of this game, they can"
          " increase your armor and max health by leveling up.\nYou can"
          " levelup by killing monsters, the more attack they do, the more exp"
          " you will get.\nExp tells you how far you need to go to level up."
          " Levels also dictate when you can fight bosses.")
    time.sleep(TUTORIAL_SLEEP)

    print("\nSkills: Skills are sometimes obtained when you levelup."
          " They can only be used against bosses. They can deal damage,"
          " or increase your stats,")
    time.sleep(TUTORIAL_SLEEP)

    print("\nBosses: Bosses are the big bad guys of the game. You have the"
          " opportunity to face them every 5 levels.\nThere are 5 bosses in"
          " total, each one with their own unique skill, dealing increasing"
          " damage per boss.\nTheir unique skill can only be used at the start"
          " of the battle. Each boss also has their own health and damage,"
          " increasing after boss.")
    time.sleep(TUTORIAL_SLEEP)

    print("\nMonsters: Each round, you will be confronted by three different"
          " monsters, each with their own attack stat, which dictates how much"
          " damage you will take if you fight the monster.\nAnd the treasure"
          " stat, which dictates how much treasure you will recieve after"
          " successfully killing the monster")
    time.sleep(TUTORIAL_SLEEP)

    print("\nGods: Gods are mystical beings. They can be find by doing"
          " something a lot of times.\nMaybe it's killing a whole bunch of"
          " monsters, maybe it's getting every skill in the game, maybe it's"
          " none of those.\nThats for you to find out as you play!")
    time.sleep(TUTORIAL_SLEEP)

    print(f"\n{'>' * 20} Tutorial {'<' * 20}")

# Player doesn't want to read the tutorial
else:
    print(f"Roger that {name}, lets get going!")
    time.sleep(TIME_SLEEP)
print(f"As this is your first time, I've prepared {STARTING_ROUNDS} rations"
      " for you to begin your journey\n")


# Game loop begins
# Stating the variables for the game
playing_game = "yes"
hades = False
hades_temp_true = False
ares = False
ares_temp = False
hecate = False
hecate_temp = False
while playing_game == "yes":
    area = "The Dark Forest"
    area_number = 0
    show_boss_requirements = False
    got_skill = False
    can_boss = False
    dead_by_boss = False
    force_field_active = False
    run_from_boss = False
    treasure_luck = 0
    bonus_chance = 40 - treasure_luck
    round_number = 1
    total_rounds = STARTING_ROUNDS
    treasure = 0
    bag_limit = 20
    bag_cost = 15
    max_health = 20
    health = max_health
    armor = 0
    armor_cost = 10
    level = 1
    levelup_exp = 10 * level
    exp = 0
    mana_cap = 50
    mana = mana_cap
    monsters_killed = 0
    boss_monsters_killed = 0
    monster_treasure_max = 5 + treasure_luck
    monster_treasure_min = 1 + treasure_luck
    monster_attack_max = 5
    monster_attack_min = 1
    regain_health = False
    regain_health_rate = 0
    boss_number = 1
    boss_level = 5
    skills = 1
    cyclops_kill_count = 0
    gorgon_kill_count = 0
    wild_centaur_kill_count = 0
    giant_kill_count = 0
    basilisk_kill_count = 0
    bonus = ""
    rta = ">"
    lta = "<"
    play_again = ""
    facing = ""
    death_output_variables = []
    monster_drops = ["+1 Regeneration Pill", "+1 Regeneration Pill",
                     "+2 Regeneration Pill", "+1 Armor", "+0.5 Armor",
                     "+0.5 Armor", "+2 Max Health", "+2 Max Health",
                     "+2 Health", "+2 Health", "+5 Health", "+5 Max Health",
                     "+1 Treasure Luck", "+1 Treasure Luck",
                     "+2 Treasure Luck", "+1 Ration", "nothing", "nothing",
                     "nothing", "nothing", "nothing", "nothing", "nothing"]
    monsters = ["Harpy", "Wild Centaur", "Basilisk", "Siren", "Cyclops",
                "Hydra", "Gorgon", "Giant", "Lamia"]
    player_skills = ["Final Assault", "Run"]
    areas = ["", "The Misty Mountains", "The Haunted Peaks", "The Haunted City",
             "The City of Monsters", "Tartarus"]

# Monster fighting loop begins
    print(f"{Fore.RED}You enter {area} with your trusty sword")
    time.sleep(TIME_SLEEP)


# Reseting the variables if the player wants to play again
    while round_number < total_rounds + 1:
        if play_again == "yes":
            area = "The Dark Forest"
            got_skill = False
            ares_temp = True
            hecate_temp = True
            boss_number = 1
            boss_level = 5
            skills = 1
            level = 1
            exp = 0
            levelup_exp = level * 10
            mana_cap = 50
            mana = mana_cap
            treasure = 0
            treasure_luck = 0
            bag_limit = 20
            bag_cost = 15
            total_rounds = STARTING_ROUNDS
            round_number = 1
            monster_treasure_max = 5 + treasure_luck
            monster_treasure_min = 1 + treasure_luck
            monster_attack_min = 1
            monster_attack_max = 5
            regain_health = False
            regain_health_rate = 0
            bonus = ""
            armor = 0
            armor_cost = 10
            max_health = 20
            health = max_health
            boss_monsters_killed = 0
            monsters_killed = 0
            cyclops_kill_count = 0
            gorgon_kill_count = 0
            wild_centaur_kill_count = 0
            giant_kill_count = 0
            basilisk_kill_count = 0
            facing = ""
            play_again = ""
            death_output_variables = []
            player_skills = ["Final Assault", "Run"]

# If the player has activated god bonuses, they get an increase in stats
# if they want to play the game after they died
        if hades is True and hades_temp_true is True:
            max_health += 30
            armor += 10
            health = max_health
            hades_temp_true = False

# Setting monster stats
        monster_treasure_max = STARTING_MONSTER_TREASURE + treasure_luck
# Choosing the monsters, removing them from the list so the same monster isnt
# chosen twice, and added them back after they have all been chosen
        fighting_monsters1 = random.choice(monsters)
        monsters.remove(fighting_monsters1)
        fighting_monsters2 = random.choice(monsters)
        monsters.remove(fighting_monsters2)
        fighting_monsters3 = random.choice(monsters)
        monsters.remove(fighting_monsters3)
        fighting_monsters = [fighting_monsters1, fighting_monsters2,
                             fighting_monsters3]
        monsters.append(fighting_monsters1)
        monsters.append(fighting_monsters2)
        monsters.append(fighting_monsters3)

# Setting the monster attack variables
        monster_attack1 = random.randint(monster_attack_min,
                                         monster_attack_max)
        monster_attack2 = random.randint(monster_attack_min,
                                         monster_attack_max)
        monster_attack3 = random.randint(monster_attack_min,
                                         monster_attack_max)

# Setting the monster treasure variables
        monster_treasure1 = random.randint(1, monster_treasure_max)
        monster_treasure2 = random.randint(1, monster_treasure_max)
        monster_treasure3 = random.randint(1, monster_treasure_max)

# Showing player round details
        if treasure > bag_limit:
            treasure = bag_limit
        health = increasehealth(health, max_health)
        print(f"\n{Fore.RED}{rta * 20} {round_number} / {total_rounds}"
              f" {lta * 20}")
        print(f"Level: {level}")
        print(f"Exp: {exp}/{levelup_exp}")
        print(f"Health: {health}/{max_health}")
        print(f"Treasure: {treasure}/{bag_limit}")
        print(f"Armor: {armor}\n")
        time.sleep(TIME_SLEEP)
        print("You have encountered 3 monsters!")
        time.sleep(TIME_SLEEP)
        print(f"You face: \n\n{fighting_monsters1} with {monster_attack1} "
              f"attack and {monster_treasure1 + treasure_luck} treasure")
        print(f"\n{fighting_monsters2} with {monster_attack2} attack and "
              f"{monster_treasure2 + treasure_luck} treasure")
        print(f"\n{fighting_monsters3} with {monster_attack3} attack and "
              f"{monster_treasure3 + treasure_luck} treasure\n")

# Asking player which monster they want to face
        while facing not in fighting_monsters:
            try:
                facing = input("Which monster do you want to face? "
                               ).title().strip()
            except ValueError:
                print("Thats not a monster")
            except IndexError:
                print("Thats not a monster")

# Comparing monster stats with player stats
        if facing == fighting_monsters1:
            facing_attack = monster_attack1
            facing_treasure = monster_treasure1 + treasure_luck
            exp += facing_attack
            if facing_attack <= armor:
                facing_attack = 0
            else:
                facing_attack -= armor

        if facing == fighting_monsters2:
            facing_attack = monster_attack2
            facing_treasure = monster_treasure2 + treasure_luck
            exp += facing_attack
            if facing_attack <= armor:
                facing_attack = 0
            else:
                facing_attack -= armor

        if facing == fighting_monsters3:
            facing_attack = monster_attack3
            facing_treasure = monster_treasure3 + treasure_luck
            exp += facing_attack
            if facing_attack <= armor:
                facing_attack = 0
            else:
                facing_attack -= armor

# Printing monster fight for the player to see
        print(f"You have chosen to fight the {facing}!")
        print("⚔️ Fighting ⚔️")
        time.sleep(TIME_SLEEP)
        print("⚔️ Fighting ⚔️")
        time.sleep(TIME_SLEEP)
        health -= facing_attack
        treasure += facing_treasure
        if facing == "Cyclops" and boss_number == 1 and level >= boss_level:
            cyclops_kill_count += 1
        if facing == "Gorgon" and boss_number == 2 and level >= boss_level:
            gorgon_kill_count += 1
        if facing == "Wild Centaur" and boss_number == 3\
           and level >= boss_level:
            wild_centaur_kill_count += 1
        if facing == "Giant" and boss_number == 4 and level >= boss_level:
            giant_kill_count += 1
        if facing == "Basilisk" and boss_number == 5 and level >= boss_level:
            basilisk_kill_count += 1
        if treasure > bag_limit:
            treasure = bag_limit
        round_number += 1

# If the player dies after facing the monster
        death_output_variables = dead(health, dead_by_boss, play_again,
                                 monsters_killed,  max_health,
                                 boss_monsters_killed, round_number,
                                 playing_game, hades_temp_true, hades,
                                 total_rounds)

        health = death_output_variables[0]
        dead_by_boss = death_output_variables[1]
        play_again = death_output_variables[2]
        round_number = death_output_variables[3]
        playing_game = death_output_variables[4]
        hades_temp_true = death_output_variables[5]
        hades = death_output_variables[6]
        death_output_variables = []

# If the player survived the monster incounter, continue playing the games
        if health >= 1 and play_again == "":
            health = increasehealth(health, max_health)  
            print(f"{Fore.RED}You survived with {health} Health remaining!")
            monsters_killed += 1
            time.sleep(TIME_SLEEP)


# If the player gains enough exp from killing monsters to level up and achieve
# higher stats like max health and armor, while also regaining some health
            if exp >= levelup_exp:
                print(f"{Fore.GREEN}Congrates {name}! You've leveled up to"
                      f" level {level + 1}!")
                time.sleep(TIME_SLEEP)
                print("Your Max Health has been increased by 1 and your"
                      " armor by 0.5 and your health has been increased"
                      f" by {max_health / 4}")

                maybe_skill = random.randint(1, 10)
                half_of_skill_chance = 10 / 2
                if maybe_skill >= half_of_skill_chance:
                    got_skill = True
                    if skills == 1:
                        print(f"Congratulations {name}! You just mastered the"
                              f" skill: Fire Ball!")
                        time.sleep(TIME_SLEEP)
                        print(f"\nMana Cost: {FIRE_BALL_SKILL_COST}")
                        print(f"Damage: {FIRE_BALL_SKILL_DAMAGE}")
                        print(f"Uses per fight: {FIRE_BALL_SKILL_USES}")
                        time.sleep(TIME_SLEEP)
                        print("\nInformation: The Fire Ball is the most basic"
                              " spell used by heroes. \nIt can deal"
                              f" {FIRE_BALL_SKILL_DAMAGE} damage, it costs"
                              f" {FIRE_BALL_SKILL_COST} mana, and it can be"
                              f" used {FIRE_BALL_SKILL_USES} time per fight."
                              "\nSkills can only be used against bosses\n")
                        skills += 1
                        player_skills.append("Fire Ball")

                    elif skills == 2:
                        print(f"Congratulations {name}! You just mastered the"
                              f" skill: Force Field!")
                        time.sleep(TIME_SLEEP)
                        print(f"\nMana Cost: {FORCE_FIELD_SKILL_COST}")
                        print("Effect: Damage Immunity One Round")
                        print(f"Uses per fight: {FORCE_FIELD_SKILL_USES}")
                        time.sleep(TIME_SLEEP)
                        print("\nInformation: The Force Field skill protects"
                              " the user from all forms of attack, it blocks"
                              " one attack from the opponent and can only be"
                              f" used {FORCE_FIELD_SKILL_USES} times per"
                              f" fight. \nIt costs {FORCE_FIELD_SKILL_COST}"
                              " mana to cast\n")
                        skills += 1
                        player_skills.append("Force Field")

                    elif skills == 3:
                        print(f"Congratulations {name}! You just mastered the"
                              f" skill: Heal!")
                        time.sleep(TIME_SLEEP)
                        print(f"\nMana Cost: {HEAL_SKILL_COST}")
                        print(f"Healing: {HEAL_SKILL_HEALING}HP")
                        print(f"Uses per fight: {HEAL_SKILL_USES}")
                        time.sleep(TIME_SLEEP)
                        print("\nInformation: The healing spell is a simple"
                              " spell that can heal the caster"
                              f" {HEAL_SKILL_HEALING}HP. \nIt costs"
                              f" {HEAL_SKILL_COST} mana and can be used"
                              f" {HEAL_SKILL_USES} times per fight.\n")
                        time.sleep(TIME_SLEEP)
                        print("\nHecate, Mistress of Magic, has noticed your"
                              " doings!\n")
                        skills += 1
                        player_skills.append("Heal")

                    elif skills == 4:
                        print(f"Congratulations {name}! You just mastered the"
                              f" skill: Meteor!")
                        time.sleep(TIME_SLEEP)
                        print(f"\nMana Cost: {METEOR_SKILL_COST}")
                        print(f"Damage: {METEOR_SKILL_DAMAGE}")
                        print(f"Uses per fight: {METEOR_SKILL_USES}")
                        time.sleep(TIME_SLEEP)
                        print("\nInformation: The Meteor skill is a powerful"
                              " skill, used only by those who have no regard"
                              " for those around them. \nIt costs"
                              f" {METEOR_SKILL_COST} mana, it deals"
                              f" {METEOR_SKILL_DAMAGE} damage, and it can be"
                              f" used {METEOR_SKILL_USES} times per fight.\n")
                        skills += 1
                        player_skills.append("Meteor")

                    elif skills == 5:
                        print(f"Congratulations {name}! You just mastered the"
                              f" skill: Mana Regeneration!")
                        time.sleep(TIME_SLEEP)
                        print(f"\nMana Cost: {MANA_REGENERATION_SKILL_COST}")
                        print(f"Effect: {MANA_REGENERATION_SKILL_EFFECT}Mp"
                              " and +2 Uses of all other skills")
                        print("Uses per fight:"
                              f" {MANA_REGENERATION_SKILL_USES}")
                        time.sleep(TIME_SLEEP)
                        print("\nInformation: The Mana regeneration is a"
                              " powerful skill only used by the most worthy."
                              " When cast, It can regenerate you mana levels"
                              f" to {MANA_REGENERATION_SKILL_EFFECT} points."
                              "\nIt can only be used "
                              f"{MANA_REGENERATION_SKILL_USES} times per fight"
                              f" and costs {MANA_REGENERATION_SKILL_COST}"
                              " Mana(Mp)\n")
                        skills += 1
                        player_skills.append("Mana Regeneration")

                    elif skills == 6:
                        print(f"Congratulations {name}! You just mastered the"
                              f" skill: Spatial Slash!")
                        time.sleep(TIME_SLEEP)
                        print(f"\nMana Cost: {SPATIAL_SLASH_SKILL_COST}")
                        print(f"Damage: {SPATIAL_SLASH_SKILL_DAMAGE}")
                        print(f"Uses per fight: {SPATIAL_SLASH_SKILL_USES}")
                        skills += 1
                        time.sleep(TIME_SLEEP)
                        print("\nInformation: The Spatial Slash is among"
                              " the strongest attack skills. It lauches a"
                              " devastating attack on the enemy, dealing"
                              f" {SPATIAL_SLASH_SKILL_DAMAGE} damage, while"
                              f" costing {SPATIAL_SLASH_SKILL_COST} mana. \nIt"
                              f" can only be used {SPATIAL_SLASH_SKILL_USES}"
                              " times per fight\n")
                        player_skills.append("Spatial Slash")
                        time.sleep(TIME_SLEEP)

# The player has encountered the god Hecate
                        if hecate is False:
                            print("\nHecate, Mistress of Magic, is aproaching"
                                  " you")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.MAGENTA}Hecate: Greetings hero. My"
                                  " name is Hecate, Mistress of Magic.")
                            time.sleep(TIME_SLEEP)
                            print("Hecate: I've been watching you for some"
                                  " time now.")
                            time.sleep(TIME_SLEEP)
                            print("Hecate: As you have now mastered all the"
                                  " skills I've left to mankind to learn, I"
                                  " shall grant you my blessings")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.GREEN}{name}: Thank you Miss"
                                       " Hecate. I am eternally grateful.")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.MAGENTA}Hecate: I shall grant you"
                                  " +300 Mana!")
                            time.sleep(TIME_SLEEP)
                            mana_cap += 300
                            hecate = True
                            hecate_temp = True

                mana_cap += 20
                mana += mana_cap
                armor += 0.5
                max_health += 1
                health += max_health / 2
                health = increasehealth(health, max_health)
                exp = 0
                level += 1
                levelup_exp += 10
                print(f"{Fore.GREEN}You now have {mana} mana!\n")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.GREEN}You gained {facing_treasure} treasure")


# Giving the player bonuses
# If player has the bonus to regenerate health every round
            maybe_bonus = random.randint(1,
                                            bonus_chance - treasure_luck)
            half_of_bonus_chance = bonus_chance / 2
            if maybe_bonus >= half_of_bonus_chance:
                bonus = random.choice(monster_drops)
                print(f"{Fore.GREEN}You found {bonus} on the {facing}")

# Player finds a pill the regains health every round
                if bonus == "+1 Regeneration Pill":
                    regain_health = True
                    regain_health_rate += 1
                    print(f"You now have {regain_health_rate} Regeneration"
                          " capabilities")
# Player finds a better pill that regains health every round
                if bonus == "+2 Regeneration Pill":
                    regain_health = True
                    regain_health_rate += 2
                    print(f"You now have {regain_health_rate} Regeneration"
                          " capabilities")

# Player finds armor to protect against monsters
                if bonus == "+0.5 Armor":
                    armor += 0.5
                    print(f"You now have {armor} Armor")

# Player finds better armor to protect against monsters
                if bonus == "+1 Armor":
                    armor += 1
                    print(f"You now have {armor} Armor")

# Player gets to fight an extra round
                if bonus == "+1 Ration":
                    total_rounds += 1
                    print("You've found and extra ration")

# Player gets a max health increase
                if bonus == "+2 Max Health":
                    max_health += 2
                    print(f"You now have {max_health} Max Health")

# Player gets a bigger max health increase
                if bonus == "+5 Max Health":
                    max_health += 5
                    print(f"You now have {max_health} Max Health")

# Player gets a health increase
                if bonus == "+2 Health":
                    health += 2
                    health = increasehealth(health, max_health)
                    print(f"You now have {health} Health")

# Player gets a bigger max health increase
                if bonus == "+5 Health":
                    health += 5
                    health = increasehealth(health, max_health)
                    print(f"You now have {health} Health")

# Player gets a luck stat which increases treasure gained from monsters
                if bonus == "+1 Treasure Luck":
                    treasure_luck += 1
                    print("Your Treasure Luck has been increased to"
                          f" {treasure_luck}")

# Player gets a bigger luck stat which increases treasure gained from monsters
                if bonus == "+2 Treasure Luck":
                    treasure_luck += 2
                    print("Your Treasure Luck has been increased to"
                          f" {treasure_luck}")

# Player didn't find any bonuses
            else:
                print("No loot on this monster :(")

            facing = ""
            health = regainhealth(regain_health, health, regain_health_rate)
            health = increasehealth(health, max_health)

# Setting up boss battles
            if level >= boss_level:

# Setting stats for boss #1
                if boss_number == 1:
                    boss_title = "Polyphemus, Lord of the Cylcops"
                    boss = "Polyphemus"
                    boss_health = CYCLOPS_HEALTH
                    boss_damage = CYCLOPS_DAMAGE
                    boss_skill = CYCLOPS_SKILL
                    boss_skill_damage = CYCLOPS_SKILL_DAMAGE
                    if show_boss_requirements is False:
                        print(f"\n{Fore.GREEN}You have entered the territory"
                              f" of {boss_title}!")
                        time.sleep(TIME_SLEEP)
                        print(f"To face him, fight {CYCLOPS_KILLS_NEEDED}"
                              " cyclops")
                        show_boss_requirements = True

                    if cyclops_kill_count >= CYCLOPS_KILLS_NEEDED:
                        can_boss = True
                        cyclops_kill_count = 0
                        gorgon_kill_count = 0
                        wild_centaur_kill_count = 0
                        giant_kill_count = 0
                        basilisk_kill_count = 0

# Setting stats for boss #2
                elif boss_number == 2:
                    boss_title = "Medusa, Queen of the Gorgons"
                    boss = "Medusa"
                    boss_health = GORGON_HEALTH
                    boss_damage = GORGON_DAMAGE
                    boss_skill = GORGON_SKILL
                    boss_skill_damage = GORGON_SKILL_DAMAGE
                    if show_boss_requirements is False:
                        print(f"\n{Fore.GREEN}You have entered the territory"
                              f" of {boss_title}!")
                        time.sleep(TIME_SLEEP)
                        print(f"To face her, fight {GORGON_KILLS_NEEDED}"
                              " gorgons")
                        show_boss_requirements = True

                    if gorgon_kill_count >= GORGON_KILLS_NEEDED:
                        can_boss = True
                        cyclops_kill_count = 0
                        gorgon_kill_count = 0
                        wild_centaur_kill_count = 0
                        giant_kill_count = 0
                        basilisk_kill_count = 0

# Setting stats for boss #3
                elif boss_number == 3:
                    boss_title = "Trikephalos, the Chimera"
                    boss = "Trikephalos"
                    boss_health = CHIMERA_HEALTH
                    boss_damage = CHIMERA_DAMAGE
                    boss_skill = CHIMERA_SKILL
                    boss_skill_damage = CHIMERA_SKILL_DAMAGE
                    if show_boss_requirements is False:
                        print(f"\n{Fore.GREEN}You have entered the territory"
                              f" of {boss_title}!")
                        time.sleep(TIME_SLEEP)
                        print(f"To face her, fight {WILD_CENTAUR_KILLS_NEEDED}"
                              " wild centaurs")
                        show_boss_requirements = True

                    if wild_centaur_kill_count >= WILD_CENTAUR_KILLS_NEEDED:
                        can_boss = True
                        cyclops_kill_count = 0
                        gorgon_kill_count = 0
                        wild_centaur_kill_count = 0
                        giant_kill_count = 0
                        basilisk_kill_count = 0

# Setting stats for boss #4
                elif boss_number == 4:
                    boss_title = "Porthyrion, King of the Giants"
                    boss = "Porthyrion"
                    boss_health = GIANT_HEALTH
                    boss_damage = GIANT_DAMAGE
                    boss_skill = GIANT_SKILL
                    boss_skill_damage = GIANT_SKILL_DAMAGE
                    if show_boss_requirements is False:
                        print(f"\n{Fore.GREEN}You have entered the territory"
                              f" of {boss_title}!")
                        time.sleep(TIME_SLEEP)
                        print(f"To face him, fight {GIANT_KILLS_NEEDED}"
                              " giants")
                        show_boss_requirements = True

                    if giant_kill_count >= GIANT_KILLS_NEEDED:
                        can_boss = True
                        cyclops_kill_count = 0
                        gorgon_kill_count = 0
                        wild_centaur_kill_count = 0
                        giant_kill_count = 0
                        basilisk_kill_count = 0

# Setting stats for boss #5
                elif boss_number == 5:
                    boss_title = "Typhon, Father of Monsters"
                    boss = "Typhon"
                    boss_health = TYPHON_HEALTH
                    boss_damage = TYPHON_DAMAGE
                    boss_skill = TYPHON_SKILL
                    boss_skill_damage = TYPHON_SKILL_DAMAGE
                    if show_boss_requirements is False:
                        print(f"\n{Fore.GREEN}You have entered the territory"
                              f" of {boss_title}!")
                        time.sleep(TIME_SLEEP)
                        print(f"To face him, fight {BASILISK_KILLS_NEEDED}"
                          " basilisks")
                        show_boss_requirements = True

                    if basilisk_kill_count >= BASILISK_KILLS_NEEDED:
                        can_boss = True
                        cyclops_kill_count = 0
                        gorgon_kill_count = 0
                        wild_centaur_kill_count = 0
                        giant_kill_count = 0
                        basilisk_kill_count = 0

                if can_boss is True:
                    print(f"\n{Fore.RED}You've encountered {boss_title}!")
                    fire_ball_remaining_uses = FIRE_BALL_SKILL_USES
                    force_field_remaining_uses = FORCE_FIELD_SKILL_USES
                    heal_remaining_uses = HEAL_SKILL_USES
                    meteor_remaining_uses = METEOR_SKILL_USES
                    mana_skill_remaining_uses = MANA_REGENERATION_SKILL_USES
                    spatial_skill_remaining_uses = SPATIAL_SLASH_SKILL_USES

# Asking the player if they want to fight the boss
                    engage = ""
                    while engage not in yes_or_no and can_boss is True:
                        if boss_number == 2:
                            print("-WARNING! This boss's first move is a one"
                                  " shot-")
                        engage = input(f"Do you wish to engage {boss_title} in"
                                       " mortal combat? ").strip()
                    can_boss = False

# If player says no, text printed, harder to find boss again
                    if engage == "no" or got_skill is False:
                        if got_skill is False:
                            print(f"{Fore.GREEN}You realise you don't have any"
                                  " skills to fight such a massive mosnter\n")
                            time.sleep(TIME_SLEEP)

                        print(f"{Fore.GREEN}You run away from {boss} as fast"
                              " as your little legs can carry you, luckily"
                              " they don't care about cowards")
                        time.sleep(TIME_SLEEP)
                        print("Good thing is, you wont be seeing them again"
                              " for a long time")
                        boss_level += 1
                        cyclops_kill_count = 0
                        gorgon_kill_count = 0
                        wild_centaur_kill_count = 0
                        giant_kill_count = 0
                        basilisk_kill_count = 0

# If the player chooses to fight the boss
                    else:
                        show_boss_requirements = False
                       
# Dialogue for when the player encounters a boss
                        if boss_number == 1:
                            print(f"{Fore.RED}\nPolyphemus: WHOS DARES ENTER"
                                  " MY HOME!")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.GREEN}{name}: My name is no-one!")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.RED}Polyphemus: YOU ARE NOT NO-ONE!"
                                  " HOW DARE YOU TRY TO TRICK ME! I'LL KILL"
                                  " YOU!\n")
                        elif boss_number == 2:
                            print(f"{Fore.GREEN}\n-Pro Tip: Do not fight"
                                  " without forcefied skill-")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.RED}Medusa: I know your here little"
                                  " hero. I can smell your fear!")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.GREEN}You quake in your boots."
                                  " You remember the tails"
                                  " the villagers told you about Medusa,"
                                  " about how she can turn"
                                  " anyone she sees to stone with a glace,"
                                  " but can only try once per hero."
                                  f"{Fore.RED}\n")
                        elif boss_number == 3:
                            print(f"{Fore.RED}\nTrikephalos: YOU DARE"
                                  " CHALLENGE ME? I AM THE CHIMERA! SLAYER OF"
                                  " HEROES, DESTROYER OF LYKIA.")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.GREEN}{name}: I really don't care."
                                  " I just need you dead")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.RED}Trikephalos: YOUR PLEA FOR DEATH"
                                  " HAS BEEN ANSWERED\n")
                        elif boss_number == 4:
                            print(f"{Fore.RED}\nPorphyrion: So mighty hero."
                                  " We meet atlast.")
                            time.sleep(TIME_SLEEP)
                            print("Porphyrion: My name is Porphyrion, and I"
                                  " am the king of giants")
                            time.sleep(TIME_SLEEP)
                            print("Porphyrion: And today you will die! You"
                                  " will drown in your own blood!")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.GREEN}{name}: Are you always this"
                                  f" rude to your guests?{Fore.RED}\n")
                        elif boss_number == 5:
                            print(f"{Fore.RED}\nTyphon: I have waited a long"
                                  " time for this punny mortal.")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.GREEN}{name}: For what? I don't"
                                  " recognise your ugly face.")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.RED}Typhon: YOU INSULENT MORTAL! I"
                                  " AM TYPHON, FATHER OF ALL MONSTERS! AND YOU"
                                  " HAVE KILLED MY BELOVED DAUGHTER,"
                                  " TRIKEPHALOS, AND MY FAVOURITE GIANT"
                                  " BROTHER, PORPHYRION!")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.GREEN}{name}: Who?")
                            time.sleep(TIME_SLEEP)
                            print(f"{Fore.RED}Typhon: AAARRRGGGHHH! YOU WILL"
                                  " NOT LIVE TO SEE ANOTHER DAY!\n")
                        time.sleep(TIME_SLEEP)
                        print(f"{rta * 20} {boss_title} VS {name} {lta * 20}")
                        time.sleep(TIME_SLEEP)
                        boss_round = 1

# Starting boss fight rounds
                        while health > 0 and boss_health > 0\
                              and run_from_boss is False:
                            health = regainhealth(regain_health, health,
                                                  regain_health_rate)
                            health = increasehealth(health, max_health)

# Showing boss and player stats
                            print(f"\n{boss}'s stats:")
                            print(f"    Health: {boss_health}")
                            print(f"    Damage per round: {boss_damage}")
                            print(f"\nSkill: {boss_skill}"
                                  f"(Damage: {boss_skill_damage})")
                            time.sleep(TIME_SLEEP)

                            print(f"\n{name}'s stats:")
                            print(f"    Mana: {mana}")
                            print(f"    Level: {level}")
                            print(f"    Exp: {exp}/{levelup_exp}")
                            print(f"    Health: {health}/{max_health}")
                            print(f"    Armor: {armor}")
                            print(f"    Treasure: {treasure}/{bag_limit}")
                            print("    Regenerate Health Rate:"
                                  f" {regain_health_rate}")
                            print("\nSkills:")
                            time.sleep(TIME_SLEEP)

# Showing player skills
                            if skills >= 2:
                                print("Fire Ball (Mana Cost:"
                                      f" {FIRE_BALL_SKILL_COST})"
                                      f"(Damage: {FIRE_BALL_SKILL_DAMAGE})"
                                      f"(Uses: {fire_ball_remaining_uses})")

                            if skills >= 3:
                                print("\nForce Field (Mana Cost:"
                                      f" {FORCE_FIELD_SKILL_COST})"
                                      "(Effect: Immunity to damage for one"
                                      " round(Uses:"
                                      f" {force_field_remaining_uses})")

                            if skills >= 4:
                                print(f"\nHeal (Mana Cost: {HEAL_SKILL_COST})"
                                      f"(Healing: {HEAL_SKILL_HEALING})"
                                      f"(Uses: {heal_remaining_uses})")

                            if skills >= 5:
                                print(f"\nMeteor (Mana Cost:"
                                      f" {METEOR_SKILL_COST})(Damage:"
                                      f" {METEOR_SKILL_DAMAGE})(Uses:"
                                      f" {meteor_remaining_uses})")

                            if skills >= 6:
                                print("\nMana Regeneration (Mana Cost:"
                                      f" {MANA_REGENERATION_SKILL_COST})"
                                      "(Effect: +"
                                      f"{MANA_REGENERATION_SKILL_EFFECT}Mp and"
                                      " +2 Uses of all other skills)(Uses:"
                                      f" {mana_skill_remaining_uses})")

                            if skills >= 7:
                                print("\nSpatial Slash (Mana Cost:"
                                      f" {SPATIAL_SLASH_SKILL_COST})"
                                      f"(Damage: {SPATIAL_SLASH_SKILL_DAMAGE})"
                                      "(Uses:"
                                      f" {spatial_skill_remaining_uses})")
                           
                            print("\nFinal Assault (Mana Cost: 0)(Damage:"
                                  f" {FINAL_ASSAULT_SKILL_DAMAGE})"
                                  "(Uses: Infinite)")
                           
                            print("\nRun (A last hope)")
                           
                            time.sleep(TIME_SLEEP)
                            print(f"\n{rta * 10}Round #{boss_round}{lta * 10}")
                            boss_round += 1
                            print("\nIt's your turn!")
                            skill_use = ""

# Asking player which skill they want to use against the boss
                            while skill_use not in player_skills:
                                skill_use = input("Which skill do you wish to"
                                                  " use? ").title().strip()

# If the skill the player chose is not usable in some way
                                if skill_use == "Fire Ball"\
                                   and fire_ball_remaining_uses <= 0:
                                    print("You've run out of uses for the"
                                          " Fire Ball skill")
                                    skill_use = ""
                                if skill_use == "Fire Ball"\
                                   and mana < FIRE_BALL_SKILL_COST:
                                    print("You don't have enough mana to use"
                                          " this skill")
                                    skill_use = ""

                                if skill_use == "Force Field"\
                                   and force_field_remaining_uses <= 0:
                                    print("You've run out of uses for the"
                                          " this skill")
                                    skill_use = ""
                                if skill_use == "Force Field"\
                                   and mana < FORCE_FIELD_SKILL_COST:
                                    print("You don't have enough mana to use"
                                          " this skill")
                                    skill_use = ""

                                if skill_use == "Heal"\
                                   and heal_remaining_uses <= 0:
                                    print("You've run out of uses for the"
                                          " this skill")
                                    skill_use = ""
                                if skill_use == "Heal"\
                                   and mana < HEAL_SKILL_COST:
                                    print("You don't have enough mana to use"
                                          " this skill")
                                    skill_use = ""

                                if skill_use == "Meteor"\
                                   and meteor_remaining_uses <= 0:
                                    print("You've run out of uses for the"
                                          " skill")
                                    skill_use = ""
                                if skill_use == "Meteor"\
                                   and mana < METEOR_SKILL_COST:
                                    print("You don't have enough mana to use"
                                          " this skill")
                                    skill_use = ""

                                if skill_use == "Mana Regeneration"\
                                   and mana_skill_remaining_uses <= 0:
                                    print("You've run out of uses for the"
                                          " skill")
                                    skill_use = ""
                                if skill_use == "Mana Regeneration"\
                                   and mana < MANA_REGENERATION_SKILL_COST:
                                    print("You don't have enough mana to use"
                                          " this skill")
                                    skill_use = ""

                                if skill_use == "Spatial Slash"\
                                   and spatial_skill_remaining_uses <= 0:
                                    print("You've run out of uses for the"
                                          " skill")
                                    skill_use = ""
                                if skill_use == "Spatial Slash"\
                                   and mana < SPATIAL_SLASH_SKILL_COST:
                                    print("You don't have enough mana to use"
                                          " this skill")
                                    skill_use = ""

# Using the skill
                            if skill_use == "Fire Ball":
                                print(f"You attacked {boss} with Fire Ball!")
                                mana -= FIRE_BALL_SKILL_COST
                                fire_ball_remaining_uses -= 1
                                boss_health -= FIRE_BALL_SKILL_DAMAGE
                                skill_use = ""
                                time.sleep(TIME_SLEEP)
                                print("🔥Launching Skill🔥")
                                time.sleep(TIME_SLEEP)
                                print("🔥Launching Skill🔥")
                                time.sleep(TIME_SLEEP)
                                print("You have dealt"
                                      f" {FIRE_BALL_SKILL_DAMAGE} damage to"
                                      f" {boss}!")

                            elif skill_use == "Force Field":
                                print("🌐You have encased yourself in an"
                                      " impenetrable force field🌐")
                                time.sleep(TIME_SLEEP)
                                mana -= FORCE_FIELD_SKILL_COST
                                force_field_remaining_uses -= 1
                                force_field_active = True
                                skill_use = ""

                            elif skill_use == "Heal":
                                print("💓You casted a healing spell and was"
                                      f" healed by {HEAL_SKILL_HEALING}Hp💓")
                                time.sleep(TIME_SLEEP)
                                mana -= HEAL_SKILL_COST
                                heal_remaining_uses -= 1
                                health += HEAL_SKILL_HEALING
                                health = increasehealth(health, max_health)
                                skill_use = ""

                            elif skill_use == "Meteor":
                                print(f"You attacked {boss} with Meteor!")
                                mana -= METEOR_SKILL_COST
                                meteor_remaining_uses -= 1
                                boss_health -= METEOR_SKILL_DAMAGE
                                skill_use = ""
                                time.sleep(TIME_SLEEP)
                                print("☄️Launching Skill☄️")
                                time.sleep(TIME_SLEEP)
                                print("☄️Launching Skill☄️")
                                time.sleep(TIME_SLEEP)
                                print("You have dealt"
                                      f" {METEOR_SKILL_DAMAGE} damage to"
                                      f" {boss}!")

                            elif skill_use == "Mana Regeneration":
                                print("💫You casted a Mana Regeneration spell."
                                      " Your mana has increased by"
                                      f" {MANA_REGENERATION_SKILL_EFFECT}Mp💫")
                                time.sleep(TIME_SLEEP)
                                mana -= MANA_REGENERATION_SKILL_COST
                                mana_skill_remaining_uses -= 1
                                mana += MANA_REGENERATION_SKILL_EFFECT
                                fire_ball_remaining_uses += 2
                                force_field_remaining_uses += 2
                                heal_remaining_uses += 2
                                meteor_remaining_uses += 2
                                spatial_skill_remaining_uses += 2
                                skill_use = ""

                            elif skill_use == "Spatial Slash":
                                print(f"You attacked {boss} with Spatial"
                                      " Slash!")
                                mana -= SPATIAL_SLASH_SKILL_COST
                                spatial_skill_remaining_uses -= 1
                                boss_health -= SPATIAL_SLASH_SKILL_DAMAGE
                                skill_use = ""
                                time.sleep(TIME_SLEEP)
                                print("🗡 Launching Skill 🗡")
                                time.sleep(TIME_SLEEP)
                                print("🗡 Launching Skill 🗡")
                                time.sleep(TIME_SLEEP)
                                print("You have dealt"
                                      f" {SPATIAL_SLASH_SKILL_DAMAGE} damage"
                                      f" to {boss}!")

                            elif skill_use == "Final Assault":
                                print(f"In a desperate act you attacked {boss}"
                                      " without any magic")
                                boss_health -= FINAL_ASSAULT_SKILL_DAMAGE
                                skill_use = ""
                                time.sleep(TIME_SLEEP)
                                print("🗡 Launching Skill 🗡")
                                time.sleep(TIME_SLEEP)
                                print("🗡 Launching Skill 🗡")
                                time.sleep(TIME_SLEEP)
                                print("You have dealt"
                                      f" {FINAL_ASSAULT_SKILL_DAMAGE} damage"
                                      f" to {boss}!")

                            elif skill_use == "Run":
                                print(f"In a desperate attempt to escape"
                                      f" {boss}, you run away as fast as you"
                                      " can.")
                                time.sleep(TIME_SLEEP)
                                print("🏃Running🏃")
                                time.sleep(TIME_SLEEP)
                                print("🏃Running🏃")
                                time.sleep(TIME_SLEEP)
                                run_from_boss = True
                                skill_use = ""
                                print("You managed to escape, but while"
                                      f" escaping, {boss} destroyed half of"
                                      " your armor and took you down to"
                                      " 0.25Hp")

# Boss's turn
                            if boss_health > 0 and run_from_boss is False:
                                print(f"\n{boss}'s Turn:")

# Special boss turn
                                if boss_round == 2:
                                    print(f"{boss}: NOW YOU'VE DONE IT\n")
                                    time.sleep(TIME_SLEEP)
                                    print(f"{boss} uses their skill:"
                                          f" {boss_skill}")
                                    print(f"{Fore.GREEN}You have been dealt"
                                          f" {boss_skill_damage} damage"
                                          f"{Fore.RED}")
                                    time.sleep(TIME_SLEEP)

# If the skill 'Force field' is active
                                    if force_field_active is True:
                                        print("Your force field has protected"
                                              " you from the attack!"
                                              f"{Fore.RED}")
                                        force_field_active = False

                                    else:
                                        health -= boss_skill_damage - armor

# Normal boss turn
                                else:
                                    print(f"{boss} attacks you, dealing"
                                          f" {boss_damage} damage")
                                    if force_field_active is True:
                                        print("Your force field has protected"
                                              " you from the attack!"
                                              f"{Fore.RED}")
                                        force_field_active = False

                                    else:
                                        health -= boss_damage - armor
                                    time.sleep(TIME_SLEEP)

# If the player defeats the boss
                        if health > 0 and boss_health <= 0:
                            if boss_number == 3:
                                print(f"\n{boss}: You may have bested me in"
                                      " combat, but you've only doomed"
                                      " yourself. My father Typhon, father of"
                                      " all monsters will come for you, and he"
                                      " WILL KILL YOU")

                            elif boss_number == 4:
                                print(f"\n{boss}: You may have won this"
                                      " battle, but my brother, Typhon, will"
                                      " finish what we have started!")

                            elif boss_number == 5:
                                print(f"\n{boss}: So you've done it. You've"
                                      " defeated me, the last thing that"
                                      " stands in your way to defeating"
                                      " olympus.\nNow there is nothing in"
                                      " your way, except for the gods"
                                      " themselves.")

                            else:
                                print(f"\n{boss}: You may have defeated me,"
                                      " but there will be more like me,"
                                      " stronger,"
                                      " smarter, AND THEY WILL KILL YOU!")

                            time.sleep(TIME_SLEEP)
                            print(f"\n{Fore.GREEN}You killed {boss_title}!")
                            boss_monsters_killed += 1
                            area_number += 1
                            area = areas[area_number]
                            mana = mana_cap

                            if boss_number == 1:
                                monster_attack_min = 5

                            else:
                                monster_attack_min *= 2

                            monster_attack_max *= 2
                            boss_number += 1
                            boss_level += 5

                            treasure = bag_limit
                            print("You have recived"
                                      f" {bag_limit - treasure} treasure for"
                                      f" defeating {boss_title}")

                            print("You have gained access to hunt monsters in"
                                  f" {area}! Monsters found there are several"
                                  " times stronger")

                            if boss_number == 6:
                                print(f"{'>' * 25}{'<' * 25}")
                                print(f"{'>'* 20} 🥳Victory!🥳 {'<' * 20}")
                                print(f"{'>' * 25}{'<' * 25}")
                                print(f"{Fore.GREEN}Congratulations {name}!"
                                      "\nYou have defeated all the evil"
                                      " monsters. You have now completed"
                                      " version 1 of this game.\nMore updates"
                                      " may come, or they may not come."
                                      "\nPlease feel free to continue fighting"
                                      " some basic monsters and continue"
                                      " getting stronger.")
                                print(f"{'>' * 25}{'<' * 25}")
                                print(f"{'>' * 20} 🥳Victory!🥳 {'<' * 20}")
                                print(f"{'>' * 25}{'<' * 25}")

# If the player is defeated by the boss
                        elif health < 0:
                            print(f"\n{Fore.GREEN}{boss_title} Has defeated"
                                  " you in combat")
                            dead_by_boss = True

# If the player runs away
                        elif run_from_boss is True:
                            run_from_boss = False
                            armor = armor / 2
                            health = 0.25


# if the player dies from the boss fight
        death_output_variables = dead(health, dead_by_boss, play_again,
                                 monsters_killed,  max_health,
                                 boss_monsters_killed, round_number,
                                 playing_game, hades_temp_true, hades,
                                 total_rounds)

        health = death_output_variables[0]
        dead_by_boss = death_output_variables[1]
        play_again = death_output_variables[2]
        round_number = death_output_variables[3]
        playing_game = death_output_variables[4]
        hades_temp_true = death_output_variables[5]
        hades = death_output_variables[6]
        death_output_variables = []

# If the player kills enough monsters, they get noticed by the god ares
        total_killed = boss_monsters_killed * 10 + monsters_killed
        if total_killed >= 50 and total_killed < 100 and ares_temp is False:
            print(f"\n{Fore.GREEN}Ares, Lord of Battle, has noticed your"
                  " efforts!")
            ares_temp = True

# If the player kills enough monsters, they get the blessing of ares
        if total_killed >= 100 and ares is False:
            print(f"\n{Fore.GREEN}Ares, Lord of battle has desended from the"
                  " heavens to great you")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.RED}Ares: Greatings young Hero! I am Ares, Lord of"
                  " all the Great Battles that have ever happened!")
            time.sleep(TIME_SLEEP)
            print("Ares: I see that you've killed ONE HUNDRED monsters!")
            time.sleep(TIME_SLEEP)
            print("Ares: Therefore! I will grant you my blessing!")
            time.sleep(TIME_SLEEP)
            print("Ares: +10 ARMOR AND +40 MAX HEALTH!")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.GREEN}{name}: Thank you lord Ares!")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.RED}Ares: Thats ARES, LORD OF ALL THE GREAT"
                  " BATTLES THAT HAVE EVER HAPPENED to you!")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.GREEN}{name}: Forgive me, Ares, Lord of all"
                  " the Great Battles that have ever happened")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.RED}Ares: That's enough chit chat, get going"
                  " before I get angry again")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.GREEN}{name}: Of course Ares, Lord of all the"
                  " Great Battles that have ever happened!")
            time.sleep(TIME_SLEEP)
            print(f"{Fore.RED}Ares: FASTER! 🔥🤬🔥\n")
            time.sleep(TIME_SLEEP)
            ares = True
            max_health += 40
            armor += 10
            print(f"You now have {armor} armor and {max_health} max health")
            time.sleep(TIME_SLEEP)


# If all the rounds are over and the player is still alive, the player stops
# fighting monsters
        if health >= 0.25 and round_number >= total_rounds + 1:
            round_number = 1
            total_rounds = 0
            health = increasehealth(health, max_health)
            print(f"\n{Fore.GREEN}Congratualtions adventurer! You survived"
                  " your trip.")
            time.sleep(TIME_SLEEP)
            print(f"You have returned from your trip in {area} with "
                  f"{health} health and {treasure} treasure.")
            time.sleep(TIME_SLEEP)
            health = max_health

# Asking if player wishes to visit the market
            shopping_trip = ""
            while shopping_trip != "yes":
                shopping_trip = input("Would you like to visit the market? "
                                      "Please answer with yes or no.(Advised)"
                                      " ").lower().strip()

                if shopping_trip != "yes" and shopping_trip != "no":
                    print("Go to the shop, or bad things will happen")

                if shopping_trip == "no":
                    print("Punishment has been delt")
                    bag_cost += 0.5
                    armor_cost += 0.5

            if shopping_trip == "yes":
                print("...Walking to the market...\n")
                time.sleep(TIME_SLEEP)
                bag_or_armor = ""
                while bag_or_armor != "no":
                    bag_or_armor_list = ["bag", "armor", "rations", "no"]
                    while bag_or_armor not in bag_or_armor_list\
                          and treasure >= 1:
                        bag_or_armor = input(f"{Fore.YELLOW}Merchant: Hello"
                                              " adventurer. Would you like a"
                                              " new bag? Maybe some better"
                                              " armor? Or just some rations? "
                                              ).lower().strip()

# Asking if player wants to buy a bag
                    if bag_or_armor == "bag":
                        time.sleep(TIME_SLEEP)
                        print("So your in the market for a bag ey?")
                        time.sleep(TIME_SLEEP)
                        print(f"I see you current bag only has {bag_limit}"
                              " pouches")
                        time.sleep(TIME_SLEEP)
                        bag_buy = ""
                        while bag_buy not in yes_or_no:
                            bag_buy = input(f"Would you like to buy a new bag"
                                            f" for ${bag_cost}? It has"
                                            f" {bag_limit + 10} pouches"
                                            " ").lower().strip()
# Player buying the bag
                        if bag_buy == "yes" and treasure >= bag_cost:
                            time.sleep(TIME_SLEEP)
                            print("Thank you for your purchase")
                            treasure -= bag_cost
                            bag_cost += 10
                            bag_limit += 10
                            bag_or_armor = ""
                            print(f"Bag Limit: {bag_limit}")
                            print(f"Treasure: {treasure}")

# If the player doesnt have enough money to buy the bag
                        elif bag_buy == "yes" and treasure <= bag_cost:
                            print("Don't try to scam me!")
                            bag_or_armor = ""
                            time.sleep(TIME_SLEEP)

# If the player doesn't want to buy bags
                        else:
                            print("If your not buying anything, get out of"
                                  " my shop!")
                            bag_or_armor = ""
                            time.sleep(TIME_SLEEP)

# Asking if player wants to buy some armor
                    if bag_or_armor == "armor":
                        time.sleep(TIME_SLEEP)
                        print("So your in the market for some armor ey?")
                        time.sleep(TIME_SLEEP)
                        print(f"I see you currently only have {armor} armor"
                              " points")
                        time.sleep(TIME_SLEEP)
                        armor_buy = ""
                        while armor_buy not in yes_or_no:
                            armor_buy = input(f"Would you like to buy 0.5"
                                              " more armor point for only"
                                              f" ${armor_cost}! "
                                              ).lower().strip()

# If the player has enough money to buy armor
                        if armor_buy == "yes" and treasure >= armor_cost:
                            print("Thank you for your purchase")
                            treasure -= armor_cost
                            armor += 0.5
                            armor_cost += 5
                            bag_or_armor = ""
                            print(f"Armor: {armor}")
                            print(f"Treasure: {treasure}")

# If the player doesnt have enough money to buy armor
                        elif armor_buy == "yes" and treasure <= armor_cost:
                            print("Don't try to scam me!")
                            bag_or_armor = ""
                            time.sleep(TIME_SLEEP)

# If the player doesnt want to buy armor
                        else:
                            print("If you dont want to buy anything then get"
                                  " out of my shop!")
                            bag_or_armor = ""

# Asking if player wants to buy some rations
                    if bag_or_armor == "rations":
                        time.sleep(TIME_SLEEP)
                        print("Oh, just some rations you say?")
                        time.sleep(TIME_SLEEP)
                        buy_rounds = 0

                        while buy_rounds <= 0:
                            try:
                                buy_rounds = int(input("How many rations do"
                                                        " you want to buy?"
                                                        " They're only $1"
                                                        " each "))

                                if buy_rounds <= 0:
                                    print("Stop being a muppit")
                                    time.sleep(TIME_SLEEP)

                            except ValueError:
                                print("Thats not a number")
                                time.sleep(TIME_SLEEP)

# If the player doesnt have enough treasure to buy all the rounds they want
                        if treasure < buy_rounds:
                            print("Dont try to scam me!")
                            time.sleep(TIME_SLEEP)
                            bag_or_armor = ""

# If the player has enough treasure to buy all the rounds they want
                        else:
                            total_rounds += buy_rounds
                            treasure -= buy_rounds
                            bag_or_armor = ""
                            buy_rounds = 0
                            print("Here ya go")
                            print(f"Rations: {total_rounds}")
                            print(f"Treasure: {treasure}")

# If the player runs out of money
                    if treasure < 1:
                        time.sleep(TIME_SLEEP)
                        print("You've run out of money, so you've left the"
                              " market")
                        bag_or_armor = "no"

                       

# Player going home instead of the shop
            time.sleep(TIME_SLEEP)
            print(f"{Fore.GREEN}Alrighty then, lets go fight some more"
                  " monsters!")
            time.sleep(TIME_SLEEP)
            if total_rounds == 0:
                total_rounds = 1

# If the player killed next to no monsters before death
if monsters_killed <= GODS_DISSAPOINTED:
    print("You have dissapointed the gods!")
    time.sleep(TIME_SLEEP)
    print("Your soul will now be sent to the fields of Punishment")

# If the player killed many monsters before death
elif boss_monsters_killed <= NOT_ENOUGH_BOSSES\
        and monsters_killed >= GODS_PLEASED:
    print("The gods are content with your outcome")
    time.sleep(TIME_SLEEP)
    print("Your soul will now be sent to the fields of Asphodel")

# If the player killed many monsters and boss monsters before death
elif boss_monsters_killed >= ENOUGH_BOSSES:
    print("The gods are very happy with your heroic actions!")
    time.sleep(TIME_SLEEP)
    print("Your soul will now be sent to Elysium, the home of heroes")
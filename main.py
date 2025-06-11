# - - - - - - - IMPORTING CLASSES - - - - - - - #

# Cave
from cave import Cave
# Character
from character import Character
from character import Enemy

# - - - - - - - CAVE INFORMATION - - - - - - - #

# Hollow
hollow = Cave('Harrowing Hollow')
hollow.set_description('Its so empty in here...')
# Cavern
cavern = Cave('Crusty Cavern')
cavern.set_description('A strangely crusty cave. The walls are... shedding?')
# Grotto
grotto = Cave('Grotty Grotto')
grotto.set_description('Filthy, grimey, grotty. Untouched since 1812.')
# Dungeon
dungeon = Cave('Dusty Dungeon')
dungeon.set_description('Theres a rustling behind the dust... maybe a splashing?')
# Lake
lake = Cave('Lukewarm Lake')
lake.set_description('A calm and tranquil lake, why dont I go for a dip?')
# Mines
mines = Cave('Merchants Mines')
mines.set_description('How neat. A one stop shop for all necessities.')
# Keep
keep = Cave('The Krakens Keep')
keep.set_description('Theres something in the water.')
# Fissure
fissure = Cave('Freaky Fissure')
fissure.set_description('Its said to be haunted in here, bah?')
# Tunnel
tunnel = Cave('Tyrannical Tunnel')
tunnel.set_description('Its so cold...')
# Rave
rave = Cave('The Cave Rave')
rave.set_description('Oh party party yah')

# - - - - - - - CAVE LINKS - - - - - - - #

# Hollow
hollow.link_cave(cavern, 'south')
# Cavern
cavern.link_cave(hollow, 'north')
cavern.link_cave(grotto, 'east')
cavern.link_cave(mines, 'south')
cavern.link_cave(dungeon, 'west')
# Grotto
grotto.link_cave(lake, 'south')
grotto.link_cave(cavern, 'east')
# Dungeon
dungeon.link_cave(cavern, 'east')
dungeon.link_cave(keep, 'south')
# Lake
lake.link_cave(grotto, 'north')
# Mines
mines.link_cave(cavern, 'north')
mines.link_cave(fissure, 'east')
mines.link_cave(tunnel, 'south')
# Keep
keep.link_cave(dungeon, 'north')
keep.link_cave(rave, 'south')
# Fissure
fissure.link_cave(mines, 'west')
# Tunnel
tunnel.link_cave(mines, 'north')
# Rave
rave.link_cave(keep, 'north')

# - - - - - - - ENEMIES - - - - - - - #

# Gribsy
gribsy = Enemy("Gribsy", "Keeper of the Caves. His IQ is beyond your comprehension.")
gribsy.set_conversation("You're wasting my time AND yours, my dear ignoramus.")
gribsy.set_weakness("Ignorance")
hollow.set_character(gribsy)

# Marmite and Kibbie (Crusty Cavern)
marmite = Enemy("Marmite", "Curious dust kitty.")
marmite.set_conversation("Marm.")
marnite.set_weakness("Crust")
cavern.set_character(marmite)

kibbie = Enemy("Kibbie", "Skittish dust kitty")
marmite.set_conversation("Kibs")
marnite.set_weakness("Dust")
cavern.set_character(kibbie)

# Humonculus (Dusty Dungeon)
humonculus = Enemy("Humonculus", "A giant beastie made of stone")
humonculus.set_conversation("Do you WANT your windshield bricked?")
humonculus.set_weakness("Feather")
dungeon.set_character(humonculus)

# Gangalang (Tyrannical Tunnel)
gangalang = Enemy("Gangalang", "Cause 3 enemies is the charm")
gangalang.set_conversation("Stop right there! Right there? RIGHT THERE!!")
gangalang.set_weakness("Marbles")
tunnel.set_character(gangalang)

# Boteko (Freaky Fissure)
boteko = Enemy("Boteko", "This guy is kind of Jank.")
boteko.set_conversation("Heart deedee, with a baby")
boteko.set_weakness("Burning wood")
fissure.set_character(boteko)

# Krakeluss - (Kraken's Keep)
krakeluss = Ememy("Krakeluss", "Hasn't seen the light of day in eons. Don't look into his eyes")
krakeluss.set_conversation("This is the end, traveller.")
krakeluss.set_weakness("Light")
keep.set_character(krakeluss)

# - - - - - - - FRIENDS - - - - - - - #

# - - - - - - - GAME LOOP - - - - - - - #

current_cave = hollow
dead = False
while dead == False:
    print('\n')
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("Choose your weaponry ")
            combat_weapon = input()
            if inhabitant.fight(combat_weapon) == True:
                print("You have defeated the enemy.")
                current_room.set_character(None)
            else:
                print("You have been defeated by the enemy")
                print("Your journey has come to an end")
                dead = True
        else:
            print("There is no enemy here to defeat")
    command = input('> ')
    current_cave = current_cave.move(command)

# - - - - - - - x - - - - - - - #
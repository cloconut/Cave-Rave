from cave import Cave

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

# Linked Caves

hollow.link_cave(cavern, 'south')

cavern.link_cave(hollow, 'north')
cavern.link_cave(grotto, 'east')
cavern.link_cave(mines, 'south')
cavern.link_cave(dungeon, 'west')

grotto.link_cave(lake, 'south')
grotto.link_cave(cavern, 'east')

dungeon.link_cave(cavern, 'east')
dungeon.link_cave(keep, 'south')

lake.link_cave(grotto, 'north')

mines.link_cave(cavern, 'north')
mines.link_cave(fissure, 'east')
mines.link_cave(tunnel, 'south')

keep.link_cave(dungeon, 'north')
keep.link_cave(rave, 'south')

fissure.link_cave(mines, 'west')

tunnel.link_cave(mines, 'north')

rave.link_cave(keep, 'north')

# Game loop
current_cave = cavern
while True:
    print('\n')
    current_cave.get_details()
    command = input('> ')
    current_cave = current_cave.move(command)
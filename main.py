from cave import Cave

hollow = Cave('Harrowing Hollow')
hollow.set_description('Its so empty in here...')
# Linked Caves
hollow.link_cave(cavern, 'south')

cavern = Cave('Crusty Cavern')
cavern.set_description('A strangely crusty cave. The walls are... shedding?')
# Linked Caves
cavern.link_cave(hollow, 'north')
cavern.link_cave(ghetto, 'east')
cavern.link_cave(mines, 'south')
cavern.link_cave(dungeon, 'west')

grotto = Cave('Grotty Grotto')
grotto.set_description('Filthy, grimey, grotty. Untouched since 1812.')
# Linked Caves
grotto.link_cave(lake, 'south')
grotto.link_cave(cavern, 'east')

dungeon = Cave('Dusty Dungeon')
dungeon.set_description('Theres a rustling behind the dust... maybe a splashing?')
# Linked Caves
dungeon.link_cave(cavern, 'east')
dungeon.link_cave(keep, 'south')

lake = Cave('Lukewarm Lake')
lake.set_description('A calm and tranquil lake, why dont I go for a dip?')
# Linked Caves
lake.link_cave(ghetto, 'north')

mines = Cave('Merchants Mines')
mines.set_description('How neat. A one stop shop for all necessities.')
# Linked Caves
mines.link_cave(cavern, 'north')
mines.link_cave(fissure, 'east')
mines.link_cave(tunnel, 'south')

keep = Cave('The Krakens Keep')
keep.set_description('Theres something in the water.')
# Linked Caves
keep.link_cave(dungeon, 'north')
keep.link_cave(cave, 'south')

fissure = Cave('Freaky Fissure')
fissure.set_description('Its said to be haunted in here, bah?')
# Linked Caves
fissure.link_cave(mines, 'west')

tunnel = Cave('Tyrannical Tunnel')
tunnel.set_description('Its so cold...')
# Linked Caves
tunnel.link_caves(mines, 'north')

cave = Cave('The Cave Rave')
cave.set_description('Oh party party yah')
# Linked Caves
cave.link_cave(keep, 'north')

cavern.describe()
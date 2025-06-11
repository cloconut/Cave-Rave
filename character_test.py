from character import Character
from character import Enemy

asriel = Enemy("Asriel Dreemurr", "The absolute GOD of hyperdeath.")
asriel.set_conversation("I don't need ANYONE!")
asriel.set_weakness("Mercy")

asriel.describe()
asriel.talk()

print("What will you fight with?")
combat_weapon = input()
asriel.fight(combat_weapon)
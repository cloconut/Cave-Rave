class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name.upper()
        self.description = char_description
        self.conversation = None
    # Describe the character
    def describe(self):
        print(self.name + ' is here!')
        print(self.description)
    # Character dialogue (default)
    def set_conversation(self, conversation):
        self.conversation = conversation
    # Interaction
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + "]: " + self.conversation)
        else:
            print(self.name + "really isn't in the mood.")
    # Initiate a fight
    def fight(self, combat_item):
        print(self.name + "isn't bothered enough.")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    # Enemy's weakness
    def set_weakness(self, weakness):
        self.weakness = weakness
    # Combat item
    def set_combat_item(self, combat_item):
        self.combat_item = combat_item
    # Initiate a fight
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("[" + self.name + "]: " + "What... is that.")
            print("You've discovered the enemy's weakness")
            print("Attacker's defense has dropped by 50%")
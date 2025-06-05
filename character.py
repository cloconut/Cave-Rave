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

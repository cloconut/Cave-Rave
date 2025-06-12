# - - - - - - - ITEM SUPERCLASS - - - - - - - #

class Item():
    def __init__(self, item_name, item_desc):
        self.name = item_name.upper()
        self.description = item_desc

    def describe(self):
        print("You stumbled across a" + self.name)
        print(self.description)



# Cave Class
class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
    # Get the cave description
    def get_description(self):
        return self.description
    # Set the cave description
    def set_description(self, cave_description):
        self.description = cave_description
    # Display the cave description
    def describe(self):
        print(self.description)
    # Get the cave name
    def get_name(self, cave_name):
        print(cave_name)
    # Set the cave name
    def set_name(self, cave_name):
        cave_name = input('What will you name this cave?')
    # Link cave method
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
import random

class Game:
    def __init__(self):
        self.locations = {
            'Beach': {
                'description': "You are on a sunny beach. You can go to the Forest or the Cave.",
                'options': ['Forest', 'Cave']
            },
            'Forest': {
                'description': "You are in a dense forest. You can go back to the Beach or to the Cave.",
                'options': ['Beach', 'Cave']
            },
            'Cave': {
                'description': "You are in a dark cave. You can go back to the Beach or search for treasure.",
                'options': ['Beach', 'Treasure']
            }
        }
        self.treasure_found = False

    def start_game(self):
        print("Welcome to Treasure Island!")
        print("Your mission is to find the treasure.\n")
        self.current_location = 'Beach'
        self.play()

    def play(self):
        while not self.treasure_found:
            print(self.locations[self.current_location]['description'])
            choice = input(f"Where do you want to go? ({', '.join(self.locations[self.current_location]['options'])}): ").strip()

            if choice in self.locations[self.current_location]['options']:
                self.current_location = choice
                if self.current_location == 'Treasure':
                    self.find_treasure()
            else:
                print("Invalid choice. Try again.")

    def find_treasure(self):
        print("You search the cave carefully...")
        if random.choice([True, False]):
            print("Congratulations! You found the treasure!")
            self.treasure_found = True
        else:
            print("Unfortunately, there is no treasure here. You should try another location.")

if __name__ == "__main__":
    game = Game()
    game.start_game()

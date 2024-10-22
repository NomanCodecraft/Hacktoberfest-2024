import random

class BandNameGenerator:
    def __init__(self):
        self.adjectives = [
            "Funky", "Mysterious", "Wild", "Electric", "Charming",
            "Radiant", "Sassy", "Dreamy", "Brave", "Sonic"
        ]
        self.nouns = [
            "Tigers", "Gorillas", "Rockets", "Pandas", "Vampires",
            "Ghosts", "Knights", "Waves", "Stars", "Dragons"
        ]
        self.genres = [
            "Rock", "Jazz", "Pop", "Metal", "Indie", "Blues",
            "Hip Hop", "Country", "Reggae", "Electronic"
        ]

    def generate_band_name(self):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        genre = random.choice(self.genres)
        return f"{adjective} {noun} of {genre}"

    def start(self):
        print("Welcome to the Band Name Generator!")
        while True:
            input("Press Enter to generate a band name...")
            band_name = self.generate_band_name()
            print(f"Your band name is: {band_name}\n")
            if input("Do you want to generate another name? (yes/no): ").strip().lower() != 'yes':
                print("Thanks for using the Band Name Generator! Goodbye!")
                break

if __name__ == "__main__":
    generator = BandNameGenerator()
    generator.start()

class Pet:
    def __init__(self, name):
        """Initialize a new pet with default stats and empty tricks list"""
        self.name = name 
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3) #Ensures hunger doesn't go below 0 and reduces it by 3
        self.happiness = min(10, self.happiness + 1) #Ensures happiness does not go beyond 10 and increases it by 1
        print(f"{self.name} is eating.")

    def sleep(self):
        self.energy = min(10, self.energy + 5) #Ensures energy does not go beyond 10 and increases it by 5
        print(f"{self.name} is sleeping.")

    def play(self):
        self.energy = max(0, self.energy -2) #Ensures the energy does not go below zero and reduces it by 2
        self.happiness = min(10, self.happiness + 2) #Ensures that happiness does not go beyond 10 and increases it by 2
        self.hunger = min(10, self.hunger + 1) #Ensures that hunger does not go beyond 10 and increases it by 1
        print(f"{self.name} is playing.")

    def train(self, trick):
        """Teaching the pet a new trick and adding it to the new list of tricks"""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")
              
    def show_tricks(self):
        """Displays all the tricks the pet knows"""
        if self.tricks:
            print(f"{self.name} knows these tricks: {self.tricks}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        """Prints the pet's current stats and learned tricks."""
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        if self.tricks:
            print(f"Tricks: {self.tricks}")

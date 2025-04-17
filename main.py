from pet import Pet #imports the Pet class from pet.py

pet = Pet("Ruthy") #Creates a pet named "Ruthy"

#Tests the pet's methods
pet.eat()
pet.play()
pet.sleep()
pet.train("roll over") #Teach Ruthy a new trick
pet.train("play daed") #Teack Ruthy a new trick

#check Ruthy's current status
pet.get_status()

#show all tricks Ruth knows
pet.show_tricks()
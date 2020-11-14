import animal
# driver code (must move to another file)
def Main():
    foxPopulation = []
    rabbitPopulation = []
    MenuOption = 0
    while MenuOption != 3:
        print ("Predator Prey Simulation Main Menu")
        print ()
        print ("1. Create foxes & rabbits")
        print ("2. Run simulation with custom settings")
        print ("3. Exit")
        print ()

        MenuOption = int(input("Select option: "))
        
        if MenuOption == 1 or MenuOption == 2:
            if MenuOption == 1:
                InitialRabbitCount = int(input("Initial number of rabbit: "))
                InitialFoxCount = int(input("Initial number of foxes: "))
                Variability = int(input("Randomness variability (percent): "))

                # create the foxes
                for idx in range(0, InitialFoxCount):
                    fx = animal.Fox(Variability)
                    # should we print fox data to screen?
                    foxPopulation.append(fx)

                # create the rabbits
                for idx in range(0, InitialRabbitCount):
                    rb = animal.Rabbit(Variability)
                    # should we print fox data to screen?
                    rabbitPopulation.append(rb)

            else:
                print('simulation not [yet] fully implemented')
                print()
                print(foxPopulation)
                print(rabbitPopulation)
                # wait for input
                input()

if __name__ == "__main__":
    Main()
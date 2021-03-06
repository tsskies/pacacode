#Variables
Health = 10
Money = 100
EnemyHealth = 0
AttackDamage = 10
EnemyDamage = 10

OPPONENTBASE = "enemy base"
LAKE = "lake"
TOWN = "town"
ARMORY = "armory"
BASE = "base"
AIRBASE = "air base"


NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"

currentRoom = TOWN
#Classes
#Creates a class called Enemy, We can use this a blueprint to create muliple enemies for our game
class enemy:
    #We are Initalizing our class saying it must have attackdamage and health when created
   def __init__(self,name,attackDamage,health):
       #Sets currently being created instance of the object cfrom the classes attackdamage and health
        self.name = name
        self.attackDamage = attackDamage
        self.health = health
    

#Functions
#Store Function
def store():
    #gobal makes our variables used inside this function the affect the variables with the same name outside the function
    global Health
    global Money
    global attackDamage
    #Health and Money are int's and need to be converted to print as a string
    print("you have "+ str(Health) +" health and "+ str(Money) +" money")
    print("You're in a store. You see a M 1 grand on the table with a 30 coin label")
    print("What do you want to do? (M1,50cal,sniper rifle leave)")
    #Gets the input from the user
    direction = raw_input()
    #Takes the user input and makes it all UPPERCASE so we can use if statements without worrying about capitalization
    direction = direction.upper()
    #Checks if the user's input was BUY
    if(direction == "BUY"):
        #Checks if the user has More than or equal the amount of money needed
        if Money >= 3:
            #the variable attackDamaged is used when the user attacks an enemy. The default is 1, this is setting the users damage up to 2 because he/she has the sword now
            attackDamage = 2
            #Taking the money used to buy the sword away from the user
            Money = Money - 3
            #Calls the main function so the user can continue the game
            main()
        #If the user doesn't have enough money, it returns the user back to the store again and ask the options again
        else:
            print("You don't have enough money")
            store()
    if(direction == "M1"):
        #Checks if the user has More than or equal the amount of money needed
        if Money >= 30:
            #the variable attackDamaged is used when the user attacks an enemy. The default is 1, this is setting the users damage up to 2 because he/she has the sword now
            attackDamage = 4
            #Taking the money used to buy the sword away from the user
            Money = Money - 20
            #Calls the main function so the user can continue the game
            main()
        #If the user doesn't have enough money, it returns the user back to the store again and ask the options again
        else:
            print("You don't have enough money")
            store()
    if(direction == "50cal"):
        #Checks if the user has More than or equal the amount of money needed
        if Money >= 30:
            #the variable attackDamaged is used when the user attacks an enemy. The default is 1, this is setting the users damage up to 2 because he/she has the sword now
            attackDamage = 6
            #Taking the money used to buy the sword away from the user
            Money = Money - 30
            #Calls the main function so the user can continue the game
            main()
        #If the user doesn't have enough money, it returns the user back to the store again and ask the options again
        else:
            print("You don't have enough money")
            store()
    if(direction == "sniper rifle"):
        #Checks if the user has More than or equal the amount of money needed
        if Money >= 30:
            #the variable attackDamaged is used when the user attacks an enemy. The default is 1, this is setting the users damage up to 2 because he/she has the sword now
            attackDamage = 8
            #Taking the money used to buy the sword away from the user
            Money = Money - 40
            #Calls the main function so the user can continue the game
            main()
        #If the user doesn't have enough money, it returns the user back to the store again and ask the options again
        else:
            print("You don't have enough money")
            store()
    #checks if the user's input is ROB. Rob was a secret option suggested by a student and doesn't show up as an option when the user enters the shop   
    elif(direction == "ROB"):
        #Like before the user has obtained the sword and has increased his/her damage. This time through steal so the user doesn't lose money
        AttackDamage = 2
        print("You steal the M1 Grand and quickly fly out the door unnoticed!")
        main()
    #Takes the user out of the store and back to the main game  
    elif(direction == "LEAVE"):
        main()
    #If the user doesn't input a vaild answer they are returned to the store to try again    
    else:
        print("Choose a vaild answer \n")
        store()
    
def dealth():
    global AttackDamage
    global Money
    global Health
    global currentRoom
    Money = 0
    Health = 1
    AttackDamage = 1
    currentRoom = TOWN
    print(" \n You've Been knocked out and all your equipment has been stolen! Fear not! a noble soul has returned you to the town.")
    main()

#The function that manages the user attacking an enemy
def attack():
    global EnemyHealth
    global EnemyDamage
    global AttackDamage
    global Money
    global Health
    #The formula for attacking an enemy
    EnemyHealth = EnemyHealth - AttackDamage
    print("You hit the enemy! The enemy has "+ str(EnemyHealth) +" remaining health")
    #Checks if the Enemy has less then our equal to 0 heal. Check if the enemy has died
    if EnemyHealth <= 0:
        print("You killed the enemy and gained some money")
        #Gives the user 1 coin for defeating an enemy
        Money = Money + 1
        #Returns the user to the main game
        main()
    #If the user has not killed his/her opponent
    else:
        print("You've been hit!")
        #The enemy attacks and takes one health away from the user
        Health = Health - EnemyDamage
        if Health <= 0:
            dealth()
        
        print("You have " + str(Health) + " health")
        #The user returns to the enocounter to decide their next combat option
        encounter()
        
#The function that manages the users combat encounters with enemies
def encounter():
    global currentRoom
    
    print("attack or flee")

    direction = raw_input()

    direction = direction.upper()
    #Checks if the user typed attack, and if so runs the attack function
    if(direction == "ATTACK"):
        attack()
    #Else checks if the user want to Flee and sends the user back to town    
    elif(direction == "FLEE"):
        #Tells the game that the user is in town on the map
        currentRoom = TOWN
        #Runs the town function that holds some discriptive text and takes the user back to main
        town()
    #If the user input an invaild answer, this returned the user back to the beginning of encounter to re ask the options
    else:
        print("Choose a vaild answer \n")
        encounter()
    
def EnemySpawn(enemy):
    global EnemyHealth
    global EnemyDamage
    global Health
    EnemyHealth = enemy.health
    EnemyDamage = enemy.attackDamage
    print("You see a "+enemy.name+"! You've been shot!")
    Health = Health - EnemyDamage
    if Health <= 0:
            dealth()
    print("You have " + str(Health) + " health")
    encounter()

# This function is runs whenever the user enters the forest
def forest():
    print("You are in the forest")
    #Launches the goblin enemy encounter
    #Note that forest doesn't return the user to main() like the other location functions,
    #This is because the goblin encounter will get the user back to main once finished
    soldire = enemy("soldire",1,5)
    EnemySpawn(Goblin)

# This function is runs whenever the user enters the lake
def lake():
    print("You are next to the lake")
    global Health
    #Heals the user if they have less then 10 health
    if Health < 10:
        print("You've been healed by the lake")
        Health = 10

    main()

# This function is runs whenever the user enters the town
def town():
    print("You are in the town")
    main()

# This function is runs whenever the user enters the cave
def cave():
    print("You are in the cave")
    #this is an example of how we could us ascii art, art that's text based
    print("      --------------")
    print("    /              I")
    print("  /                I")
    print(" /                 I")
    print(" I                 I")
    print(" I                 I")
    print(" I                 I")
    print(" IOOOOOOOOOOOOOOOOOI")
    print(" IOOOOOOOOOOOOOOOOOI")
    print("  \--------------/")
    gunner = enemy("gunner",3,10)
    EnemySpawn(Troll)

# This function tells the user where they are and were they can go
def look():
    # \n means new line and makes sure there's a gap between the last string or text printed to the screen.
    #We're using here for readablity, so there isn't too much text on the screen at once
    print("\n")
    if(currentRoom == TOWN):
        print("You are in a town. To your north you see a lake, to the east a forest")
    elif(currentRoom == LAKE):
        print("You are next to a lake. To your east you see a cave, to the south a town")
    elif(currentRoom == CAVE):
        print("You are in a cave. To your west you see a lake, to the south a forest")
    elif(currentRoom == FOREST):
        print("You are in the forest. To your north you see a cave, to the west a town")
    main()
        
#This function manages user movement
def choosepath():
    global currentRoom
    direction = ""

    print("Choose your direction (north, south, east, or west)")

    direction = raw_input()

    direction = direction.upper()

    #Each if statment below is used by getting the users current location "currentRoom" and direction to get to specific location
    #The if statments are separated by the location it goes to if correct
    
    # how to get to the lake
    # Checks if the location "currentRoom" is TOWN and if the direction the user wants to go is NORTH
    # If so it sets the current room to the LAKE
    if(currentRoom == TOWN and direction == "NORTH"):
        currentRoom = LAKE
    elif(currentRoom == CAVE and direction == "WEST"):
        currentRoom = LAKE

    # how to get to the cave
    elif(currentRoom == LAKE and direction == "EAST"):
        currentRoom = CAVE
    elif(currentRoom == FOREST and direction == "NORTH"):
        currentRoom = CAVE

    # how to get to the forest
    elif(currentRoom == CAVE and direction == "SOUTH"):
        currentRoom = FOREST
    elif(currentRoom == TOWN and direction == "EAST"):
        currentRoom = FOREST
    
    # how to get to the cave
    elif(currentRoom == LAKE and direction == "SOUTH"):
        currentRoom = TOWN
    elif(currentRoom == FOREST and direction == "WEST"):
        currentRoom = TOWN

    #checks the now new currentRoom and runs the function for that location
    if(currentRoom == TOWN):
        town()
    elif(currentRoom == LAKE):
        lake()
    elif(currentRoom == CAVE):
        cave()
    elif(currentRoom == FOREST):
        forest()          

#This function manages our game and is called main because it's where the user will spend the most time
#It is the backbone of our game       
def main():   
    global Health
    global Money
    global currentRoom
    print("you have "+ str(Health) +" health and "+ str(Money) +" money")
    #Checks if the location is TOWN so it can add shop as an option for the user
    if currentRoom == TOWN:
        print("What do you want to do? (look, move, store)")
    else:
        print("What do you want to do? (look, move)")

    direction = raw_input()

    direction = direction.upper()
    #Checks if the location is TOWN so it can add shop as an option for the user
    if currentRoom == TOWN:
        if(direction == "MOVE"):
            #Runs the function incharge of movement
            #It should be noted that calling a function stops the program from continuing from it's current location
            #so choosepath() will jump the program and run the first line of the Function choosepath() and not Continue main()'s next line elif(direction == "LOOK"):
            choosepath()
        elif(direction == "LOOK"):
            look()
        elif(direction == "STORE"):
            store()
        else:
            print("Choose a vaild answer \n")
            main()
    #if not town, we still need to ask the standard two questions MOVE and LOOK
    else:
        if(direction == "MOVE"):
            choosepath()
        elif(direction == "LOOK"):
            look()
        else:
            print("Choose a vaild answer \n")
            main()
    
    
town()
main()

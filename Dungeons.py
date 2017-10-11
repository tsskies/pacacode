Health = 10
Money = 0
EnemyHealth = 0
AttackDamage = 1

FOREST = "forest"
LAKE = "lake"
TOWN = "town"
CAVE = "cave"

NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"

currentRoom = TOWN

def store():
    global Health
    global Money
    print("you have "+ str(Health) +" health and "+ str(Money) +" money")
    print("You're in a store. You see a wooden sword on the table with a 3 coin label")
    print("What do you want to do? (buy, leave)")

    direction = raw_input()

    direction = direction.upper()

    if(direction == "BUY"):
        if Money >= 3:
            global attackDamage
            attackDamage = 2
            Money = Money - 3
            main()
        else:
            print("You don't have enough money")
            store()
        
    elif(direction == "ROB"):
        global AttackDamage
        AttackDamage = 2
        main()
        
    elif(direction == "LEAVE"):
        main()
    else:
        print("Choose a vaild answer \n")
        store()
    

def attack():
    global EnemyHealth
    global AttackDamage
    print(AttackDamage)
    EnemyHealth = EnemyHealth - AttackDamage
    print("You hit the enemy! The enemy has "+ str(EnemyHealth) +" remaining health")
    if EnemyHealth <= 0:
        print("You killed the enemy and gained some money")
        global Money
        Money = Money + 1
        main()
    else:
        print("You've been hit!")
        global Health
        Health = Health - 1
        print("You have " + str(Health) + " health")
        encounter()
        

def encounter():
    print("attack or flee")
    direction = raw_input()

    direction = direction.upper()

    if(direction == "ATTACK"):
        attack()
    elif(direction == "FLEE"):
        global currentRoom
        currentRoom = TOWN
        town()
    else:
        print("Choose a vaild answer \n")
        encounter()
    
def goblin():
    global EnemyHealth
    EnemyHealth = 5
    print("You see a goblin! You've been hit!")
    global Health
    Health = Health - 1
    print("You have " + str(Health) + " health")
    encounter()

def forest():
    print("You are in the forest")
    goblin()

def lake():
    print("You are next to the lake")
    global Health

    if Health < 10:
        print("You've been healed by the lake")
        Health = 10

    main()

def town():
    print("You are in the town")
    main()

def cave():
    print("You are in the cave")
    main()

def look():
    print("\n")
    if(currentRoom == TOWN):
        print("You are in a town. To your north you see a lake, to the east a forest")
    elif(currentRoom == LAKE):
        print("You are next to a lake. To your east you see a cave, to the south a town")
    elif(currentRoom == CAVE):
        print("You are in a cave. To your east you see a lake, to the south a forest")
    elif(currentRoom == FOREST):
        print("You are in the forest. To your north you see a cave, to the west a town")
    main()
        

def choosepath():
    global currentRoom
    direction = ""

    print("Choose your direction (north, south, east, or west)")

    direction = raw_input()

    direction = direction.upper()

    #print(direction)

    # how to get to the lake
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

    if(currentRoom == TOWN):
        town()
    elif(currentRoom == LAKE):
        lake()
    elif(currentRoom == CAVE):
        cave()
    elif(currentRoom == FOREST):
        forest()          


def main():
    global Health
    global Money
    global currentRoom
    print("you have "+ str(Health) +" health and "+ str(Money) +" money")
    if currentRoom == TOWN:
        print("What do you want to do? (look, move, store)")
    else:
        print("What do you want to do? (look, move)")

    direction = raw_input()

    direction = direction.upper()

    if currentRoom == TOWN:
        if(direction == "MOVE"):
            choosepath()
        elif(direction == "LOOK"):
            look()
        elif(direction == "STORE"):
            store()
        else:
            print("Choose a vaild answer \n")
            main()
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

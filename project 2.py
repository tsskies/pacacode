def GetPlayerInput():
    PlayerInput= raw_input()
    PlayerInput.upper()
    if (PlayerInput == "A"):
        return("A")
    elif (PlayerInput == "B"):
        return("B")
    elif (PlayerInput == "C"):
        return("C")
    else:
        print("Choose a valid answer")
        GetPlayerInput()
    return("D")




   
print("Zane:")
print("     .: Casually writes in the book: What the-- How'd you get here?")
print("You want to save your people, how do you think you can stop me?")

print("\nA. A Princess To Save You?")
print("\nB. Fight For Yourself?")
print("\nC. Ignore The Problem?")
x = GetPlayerInput()

if (x == "A"):
    print("Zane:")
    print("  What are you crazy or something? Princess Abbie Is Weak!")
    print("Well, Go Ahead, Try And Stop Me.")

if (x == "B"):
    print("Zane:")
    print(" Think you can fight for yourself? I admire your courage.")
    print("Good luck, stay safe.")

if (x == "C"):
    print("Zane:")
    print(" You think you can ignore this?")
    print("You're dead!")

    print("What's this? it looks like you died!")

    print("\nA. Go save the wolves?")
    print("\nB. Confront the villians?")
    print("\nC. Contact the princess?")

x = GetPlayerInput() 
          

if (x == "A"):
          print("Zane:")
          print(" That's harder than you think!")
          print(" It looks like you have accomplished your goal. Congrats, you won!")

if (x == "B"):
                print("Zane:")
                print("Oh, Hannah and the gang are you beatable.")

                print("OH NO! You died an awful death to Hannah and her twin brother Thomas.")

if (x == "C"):
                print("Zane:")
                print("As I said, Abbie is weak.")

                print("You and Princess Abbie fought bravely, sadly you have died, but princess Abbie won the battle.")
                print("YAY! Princess Abbie won the game for you. Try to do your work for yourself.")
    

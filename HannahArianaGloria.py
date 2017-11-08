

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
    print("  What are you stupid or something? Princess Abbie Is Weak!")
    print("Welp, Go Ahead, Try And Stop Me.")

if (x == "B"):
    print("Zane:")
    print(" Think you can fight for yourself? I admire your courage.")

if (x == "C"):
    print("Zane:")
    print(" You think you can ignore this?")
    print("You're dead!")

    print("What's this? it looks like you died!")


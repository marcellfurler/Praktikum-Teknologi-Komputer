#Zhivaldo Fabio
#71200608

name = input("STATE YOUR NAME: ")

print ("="*100, "\n")

print ("<"*10, "Adventure of", name, ">"*10)
print ()
print ("Welcome to the Adventure of", name + "!")
print ()
gender = input("Are you a Male / Female? [M/F]\n>> ")
print ("\n\n")
print ("One day, A young adventurer named", name, "\nspawned in a peacefull Village of Orion")
print (name, "walked out of village and see a slime jumping around.")
print ()
weapon = input("picked up a... (Sword/Bow)\n>> ")
print ("and attack the slime.")

if weapon in ("Sword", "sword"):
    print ("the slime get sliced and died. adventurer gain a level.")
    print ()
    print (name, "The Adventurer, then run towards a chest that glows from the inside")
    choice2 = input("PICK ONE!\n[OPEN/WALK]\n>> ")
    if choice2 in ("Open", "open"):
        print ()
        print ("The Adventurer Finds a Gold and brings it Home to the Village.")
        print ()
        if gender == "M":
            print ("as the adventure walks, he started to feel more and more tired.")
        elif gender == "F":
            print ("as the adventure walks, she started to feel more and more tired.")
        else:
            print ("Error")
            exit()

        choice3 = input("Take a [Break] / Keep [Walk]ing\n>> ")
        if choice3 in ("Break", "break"):
            print()
            print (name, "Died eaten by the wolfes")
        elif choice3 in ("Walk", "walk"):
            print()
            print (name, "Arrived at the village and see RTX 3090 Ti on sale\nWith the price of 1 gold")
            choice4 = input("[BUY] / [PASS]>> ")
            if choice4 in ("BUY", "buy", "Buy"):
                print ("Congratulation! you got your dream stuff! \nNow you can play Minecraft with Raytracing FOREVER! \n\nAnd live Happily ever After!~~")
            if choice4 in ("PASS", "Pass", "pass"):
                print ("UNLUCKY! you missed the chance and all peripheral price rocketly increase. \nYou get sad and killed yourself of desperation.")
        

    elif choice2 in ("Walk", "walk"):
        print ()
        print ("Adventurer walks and fall into a pit and died.")
    
elif weapon in ("Bow", "bow"):
    print ("You missed and Died.")

else :
    print ("Error")
    input ("press ENTER TO EXIT")
    

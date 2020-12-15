#setup
import time

counter = 0
solved = "False"
inventory = []
explore = "Nothing"
area = "None"
purse = "None"
guards = "No"
bribe = "Nothing"
weapon = "Nothing"
weaponownership = "No"
information = "unattained"
useinfo = "None"

#coding
def intro():
    print("You are on a boat returning to your home in the icy north.")
    time.sleep(1)
    print("Soon, the port will be filled with ice and your small village")
    time.sleep(1)
    print("will be all alone and have no contact with the rest of the world.")
    time.sleep(1)
    print("In the middle of the night, you hear a crash, what will you do?")

def choice():
    global explore
    while explore != "Yes" and explore != "No":
        explore = input("Will you check out the noise? (Yes or No): ")

def result():
    global counter
    if explore == "Yes":
        print("You go outside and look around...")
        time.sleep(1)
        print("You hear a scream and begin running in the direction of the screams.")
        time.sleep(1)
        print("Upon your arrival, you find,")
        time.sleep(2)
        print("A DEAD BODY!")
        time.sleep(1)
        print("Multiple other villagers have emerged from their homes,")
        time.sleep(1)
        print("and see you standing above the dead body.")
        time.sleep(2)
        print("You are accused of murder, but there isn't enough evidence to arrest you yet.")
        counter -= 1
        print("Score: {}".format(counter))
    elif explore == "No":
        print("You go back to sleep and ignore the noise,")
        time.sleep(1)
        print("however, it weighs on your mind until you wake up in the morning.")
        time.sleep(2)
        print("In the morning, the entire village is called together.")
        time.sleep(1)
        print("The previous night, someone had died!")
        time.sleep(1)
        print("Multiple people are placed under suspicion if they were awake, or seen in the area.")
        time.sleep(1)
        print("You are cleared of suspicion because multiple people confirmed that you were in your house.")
        counter += 1
        print("Score: {}".format(counter))

def investigate():
    global solved
    global inventory
    global area
    global purse
    global guards
    global bribe
    global weapon
    global weaponownership
    global information
    global counter
    global useinfo
    
    if explore == "Yes":
        print("You are under heavy suspicion, but you must find a way to clear your name.")
        time.sleep(1)
        while solved == "False":
            while area != "Crime Scene" and area != "Outskirts" and area !="Tavern":
                print("Inventory: {}".format(inventory))
                print("Where would you like to search?")
                area = input("(Crime Scene, Outskirts, Tavern) ")
                if area == "Crime Scene":
                    if guards == "No":
                        if 'Money' in inventory:
                            print("As you attempt to approach the crime scene, the village guards block your path.")
                            time.sleep(1)
                            print("Due to the heavy suspicion that's been placed on you,")
                            time.sleep(1)
                            print("they won't let you near the crime scene.")
                            time.sleep(1)
                            print("Suddenly, you remember the money in your pocket.")
                            while bribe != "Yes" and bribe != "No":
                                print("Bribe the guards?")
                                bribe = input("Yes or No? ")
                                if bribe == "Yes":
                                    inventory.remove('Money')
                                    print("The guards give you a little wink and let you pass.")
                                    guards = "Yes"
                                    counter += 1
                            bribe = "None"
                        else:
                            print("As you attempt to approach the crime scene, the village guards block your path.")
                            time.sleep(1)
                            print("Due to the heavy suspicion that's been placed on you,")
                            time.sleep(1)
                            print("they won't let you near the crime scene.")
                    elif guards == "Yes":
                        if 'Information' in inventory:
                            while useinfo != "Yes" and useinfo != "No":
                                print("Use the information?")
                                useinfo = input("Yes or No? ")
                                if useinfo == "Yes":    
                                    print("You finally connect the dots,")
                                    time.sleep(1)
                                    print("and realize that the giant snake that's been viewed in the outskirts is the culprit.")
                                    counter += 1
                                    time.sleep(1)
                                    solved = "True"
                                else:
                                    print("You enter the victim's house.")
                                    time.sleep(1)
                                    if weaponownership != "Yes":
                                        print("You notice a large, gaping hole as well as a weapon on the ground.")
                                        print("Take the weapon?")
                                        while weapon != "Yes" and weapon != "No":    
                                            weapon = input("Yes or No? ")
                                            if weapon == "Yes":
                                                inventory.append("Weapon")
                                                weaponownership = "Yes"
                                                counter += 1
                                        weapon = "None"
                                    elif weaponownership == "Yes":
                                        print("You notice a large, gaping hole.")
                            useinfo = "None"
                        else:
                            print("You enter the victim's house.")
                            time.sleep(1)
                            if weaponownership != "Yes":
                                print("You notice a large, gaping hole as well as a weapon on the ground.")
                                print("Take the weapon?")
                                while weapon != "Yes" and weapon != "No":    
                                    weapon = input("Yes or No? ")
                                    if weapon == "Yes":
                                        inventory.append("Weapon")
                                        weaponownership = "Yes"
                                        counter += 1
                                weapon = "None"
                            elif weaponownership == "Yes":
                                print("You notice a large, gaping hole.")
                elif area == "Outskirts":
                    if purse != "Yes":  
                        print("There isn't much out here, just the vast, endless ice.")
                        time.sleep(1)
                        print("As you stare out, you get an ominous feeling, and decide to leave.")
                        time.sleep(1)
                        print("You look down, and find a purse somebody dropped on the ground.")
                        time.sleep(1)
                        while purse != "Yes" and purse != "No":
                            print("Will you take it?")
                            purse = input("Yes or No?: ")
                            if purse == "Yes":
                                inventory.append("Money")
                                counter += 1
                                print("Score: {}".format(counter))
                        if purse == "No":
                            purse = "None"
                    else:  
                        print("There's nothing but the endless sea of ice.")
                elif area == "Tavern":
                    print("As you enter the tavern, most people ignore you.")
                    if information == "attained":
                        print("Doesn't seem like there's much going on here...")
                    else:
                        if 'Weapon' in inventory:
                            print("The people in the tavern notice your weapon and have you arrested.")
                            time.sleep(1)
                            counter -= 1
                            print("You Lost! Final Score: {}".format(counter))
                            exit()
                        else:
                            print("You hear some of the people talking.")
                            time.sleep(1)
                            print("You eavesdrop, and hear them mention a giant snake.")
                            time.sleep(1)
                            print("Out in the wastelands, some sort of giant snake had been spotted wrecking things.")
                            information = "attained"
                            counter += 1
                            inventory.append("Information")
                if solved == "True":
                    break
                else:    
                    area = "None"
        print("You run off towards the Outskirts.")
        time.sleep(1)
        print("When you arrive, you find the gargantuan snake.")
        if 'Weapon' in inventory:
            print("You pull out the weapon you obtained from the house, and slay the foul beast.")
            time.sleep(2)
            print("The villagers all congratulate you and apolgize for suspecting you.")
            counter += 1
            time.sleep(1)
            print("Congratulations, You Win! Score: {}".format(counter))
        else: 
            print("The enormous snake notices you and turns to face you.")
            print("It was at that moment, you realize, you messed up.")
            print("The snake swallows you whole and you die with false accusations to your name.")
            counter -= 1
            print("You Lost! Final Score: {}".format(counter))
    if explore == "No":
        print("You are determined to solve this crime.")
        time.sleep(1)
        while solved == "False":
            while area not in ["Crime Scene", "Outskirts","Tavern"]:
                print("Inventory: {}".format(inventory))
                print("Where would you like to search?")
                area = input("(Crime Scene, Outskirts, Tavern) ")
                if area == "Crime Scene":
                    if 'Information' in inventory:
                        while useinfo != "Yes" and useinfo != "No":
                            print("Use the information?")
                            useinfo = input("Yes or No? ")
                            if useinfo == "Yes":    
                                print("You finally connect the dots,")
                                time.sleep(1)
                                print("and realize that the giant snake that's been viewed in the outskirts is the culprit.")
                                counter += 1
                                time.sleep(1)
                                solved = "True"
                            else:
                                print("You enter the victim's house.")
                                time.sleep(1)
                                if weaponownership != "Yes":
                                    print("You notice a large, gaping hole as well as a weapon on the ground.")
                                    print("Take the weapon?")
                                    while weapon != "Yes" and weapon != "No":    
                                        weapon = input("Yes or No? ")
                                        if weapon == "Yes":
                                            inventory.append("Weapon")
                                            weaponownership = "Yes"
                                            counter += 1
                                weapon = "None"
                                elif weaponownership == "Yes":
                                    print("You notice a large, gaping hole.")
                    else:
                        print("You enter the victim's house.")
                        time.sleep(1)
                        if weaponownership != "Yes":
                            print("You notice a large, gaping hole as well as a weapon on the ground.")
                            print("Take the weapon?")
                            while weapon != "Yes" and weapon != "No":    
                                weapon = input("Yes or No? ")
                                if weapon == "Yes":
                                    inventory.append("Weapon")
                                    weaponownership = "Yes"
                                    counter += 1
                            weapon = "None"
                        elif weaponownership == "Yes":
                            print("You notice a large, gaping hole.")
                    useinfo = "None"
                elif area == "Outskirts":
                    if purse != "Yes":  
                        print("There isn't much out here, just the vast, endless ice.")
                        time.sleep(1)
                        print("As you stare out, you get an ominous feeling, and decide to leave.")
                        time.sleep(1)
                        print("You look down, and find a purse somebody dropped on the ground.")
                        time.sleep(1)
                        while purse != "Yes" and purse != "No":
                            print("Will you take it?")
                            purse = input("Yes or No?: ")
                            if purse == "Yes":
                                inventory.append("Money")
                                counter += 1
                                print("Score: {}".format(counter))
                        if purse == "No":
                            purse = "None"
                    else:  
                        print("There's nothing but the endless sea of ice.")
                elif area == "Tavern":
                    print("As you enter the tavern, most people ignore you.")
                    if information == "attained":
                        print("Doesn't seem like there's much going on here...")
                    else:
                        print("You try approaching a group of people and ask for any rumors.")
                        time.sleep(1)
                        print("They tell you that if you want information, you have to pay for it.")
                        time.sleep(1)
                        if 'Money' in inventory:
                            print("You remember the money you got earlier.")
                            while bribe != "Yes" and bribe != "No":
                                print("Pay for information?")
                                bribe = input("Yes or No? ")
                                if bribe == "Yes":
                                    print("The group smiles and tells you about a large snake spotted in the outskirts.")
                                    inventory.append("Information")
                                    inventory.remove('Money')
                                    counter += 1
                                elif bribe == "No":
                                    print("You leave the tavern.")
                            bribe = "None"
                        else:
                            print("You're flat broke, so you leave.")
                if solved == "True":
                    break
                else:    
                    area = "None"
        print("You run off towards the Outskirts.")
        time.sleep(1)
        print("When you arrive, you find the gargantuan snake.")
        if 'Weapon' in inventory:
            print("You pull out the weapon you obtained from the house, and slay the foul beast.")
            time.sleep(2)
            print("The villagers all congratulate you and thank you for your efforts.")
            counter += 1
            time.sleep(1)
            print("Congratulations, You Win! Score: {}".format(counter))
        else: 
            print("The enormous snake notices you and turns to face you.")
            print("It was at that moment, you realize, you messed up.")
            print("The snake swallows you whole and you die with nobody knowing what happened to you.")
            counter -= 1
            print("You Lost! Final Score: {}".format(counter))

#game progression   
print("Welcome to Ice")
time.sleep(2)
intro()
choice()
result()
investigate()

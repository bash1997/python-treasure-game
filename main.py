#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print(input("Continue? "))

print("\n\nWhile sitting at a bar, hoping to get some information on where to start")
print("you over here a troll and a mage talking.")
print("\n\"Yeah, man! If you just go down to Water Milk Bridge, and tell my cousin")
print("I sent you, you can just take that shortcut through the woods to the Dragon Lord's lair.\"")
print(input("Continue? "))

print("\n\n\n" + '''                            #########                      
                         ######                            
                    ___###___________                      
             _,--"""_________________"""--._               
           /',--'\\"##           __  "//'--.'\   ,  /\    _
 -._  /\  //'   ##\\       ,-_,-'  \_///\,-'`\\-' \/  \,-' 
    \/  \//    _  _\\ ,-._/         //'       \\           
        //'--._M_|H|\\___   ___   _//   ___   _\\   ___    
       | |    (|   | \\  | |   | |// | |   | | | | |   |   
    ___| |   /ooo=oo-o\\oo-oo=oo-//=oo-oo=oo-oo| |=oo=oo___
         \"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"'"|           
          |    \                           .   /           
    .      \   /\            .  -     '    .  /            
            `-.  '-..     ' '          ,  ,,-'     `       
               \     '- '            ,/,-'/                
     \          \_- ' '             --',-'                 
               -'                    \/            |       
      |  _  -                          - _        .       
                                                 /   ''')

print("\"You say my cousin sent?")
print("Was it my cousin with scar under his left eye or his right?\"")
left = input("Left or Right? ")
left = left.lower()
if ( left == "left") or ( left == "l"):
	print("\"RIGHT! My little cousin Swifty! God I hate him.")
	print("But family is family.")
	print("So, the water is very high during this time of day.")
	print("Only way to cross is to swim or wait for the ferry to come back.\"")

	wait = input("Swim or Wait? ")
	wait = wait.lower()
	if wait == "wait" or wait == "w" :
		print("You make it safely across the river. Yay!!")
		print(input("Continue? "))

		print('''                                 I'i___i'I                    
                                 |:|:::|:|                     
           -./~-./~-./~-./~-./~-.L_I_&_L_I.-~\.-~\.-~\.-~\.-~\.-
           fsc'\~-'\~-'\~-'\~-'\~-'     '-~/'-~/'-~/'-~/'-~/'-~/''')
		print("The troll wasn't lying about the shortcut, you soon make it to the lair.")
		print("As soon as you walk up, you notice there is a lizard man in a nice suit.")
		print("\"Very few make it this far. Pick the right door and you can have my the gold.\"")
		print(input("Continue? "))

		print("The YELLOW door is filled with white")
		print("The BLUE door is filled with green")
		print ("The RED door is filled with orange")

		yellow = input("Yellow, Blue or Red? ")
		yellow = yellow.lower()
		if yellow == "yellow" or yellow == "y":
			print("You picked the YELLOW door. As soon as you open the door...")
			print(input("Continue... "))
			print("GOLD just spills out the room, crushing the Dragon Lord!")
			print("You are named the new Dragon Lord! Hooray!!!!")
			print("You win! Game Over!")
		elif yellow == "blue" or yellow == "b":
			print("You picked the BLUE door. When you walk in, you see that its filled")
			print("with grass and trees and ...")
			print(input("Continue... "))
			print("BEASTS!!!!")
			print("You're eaten alive! Game Over!")
		elif yellow == "red" or yellow =="r":
			print("You picked the RED door. When you walk in, the room is dark but")
			print("you see something bright in the middle of the room.")
			print("When you get closer, you begin to see the full picture. It is a shiny...")
			print(input("Continue... "))
			print("DRAGON!!!")
			print("Upset that you awakened him, he burns you alive. Game Over!")
		else:
			print(f"You notice that there is a fourth door, and it is {yellow}.")
			print("Not trusting the Dragon Lord, you pick that one.")
			print("Instantly, the Dragon Lord laughs very menacing.")
			print("\"You can't have my gold, but I will feed you to my dragon\" Game Over.")
	# elif wait == "":
	# 	wait = input("Swim or Wait? ")
	else:
		print("You decide to swim across, but the current is too strong.")
		print("You get pushed downstream and off the cliff. Game Over!")
else:
	print("The troll's cousin drags you deep in the woods.")
	print("You are forever locked in a prison for lying. Game Over!")

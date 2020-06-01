## Choose your Adventure interactive Haunted House -- 5 different forks in paths (choosing rooms)
# solve math problems to defeat monsters
print("\n")
print("Please store your name and age. . .")
print("\n")
your_name = input("Enter your name \n")
your_age = input("Enter your age \n")
print("\n")
is_female = True  # Boolean value true/false
print("Hello there, " + your_name + ". . . ")
print("\n")
print("You are walking through an old growth forest somewhere in the world.")
print("There is a chill in the night air")
print("Everything around is still except for the fog that swirls continuously around your feet as you walk")
print("Not even the smallest, most hidden crickets are chirping")
print("You come across a fork in your path.")
print("\n")
print("To the left is a clearing with thousands of green moths silently fluttering above the brush")
print("To the right is a river whose water seems to have a feint luminescence. You hear its fresh water carrying off in the distance")
path_1=input("Will you go 1. left to the clearing, or 2. right to the river? \n")
path_1=int(path_1) #you have to define the input as an integer for it to work with conditional, below
if path_1 == 1: # you need two = signs for python conditionals
    print("You walk into the clearing.")
    print("You look up and can see the moon through the sudden break in tree cover.")
    print("Illuminated by the moon, the moths take on a surreal appearance against the deep blue of the night sky")
    print("You notice that the sky is peppered with bats that swoop down all around you to catch the moths.")
    print("Suddenly you hear a whisper from above '" + your_name + "'. . .")
    print("It's one of the moths! It seems friendly.")
    print("'"+your_name+ ", you are in imminent danger, as are we.' voiced another moth")
    print("'If you can save us from the bats, we can help you on your journey.' \n")
    path_1A = input("'Will you 1. save the moths or 2. keep walking? \n")
    path_1A=int(path_1A) # define as integer
    if path_1A == 1 :  #elif = elseif if you have more than two choices
        print("You quickly think of your backpack and hold it open for the moths to take refuge inside.")
        print("All the moths pour into your pack in one fluid movement. You rapidly close the bag.")
        print("The hungry bats fly sadly away to search for their supper.")
        print("When you are sure that you are alone, you open your pack and your new friends fly out")
        print("'You had better take the magic seeds, but you must only take 5, or the seeds will not root'")
        print("'Follow us; we will take you to the seeds' one moth whispered. The moths formed a path for you to follow")
        print(". . .")
    else:
        print("'I'm deeply sorry' you say as you walk on past them, 'but bats have to eat, too.'")
else:
    print("You hear beautiful music from below the water")
print("\n")
print("You have been walking through the woods all night now, and trip on something on the forest floor")
print("covered by the ferns and dirt, you see an old book")
has_MinaHarkerjournal = input("Do you pick it up? \n")#if has_MinaHarkerjournal = True: she can use it to learn secrets
print("\n")
print("you bend down and dust off the molding book. It reads 'Mina Harker's Journal'")
print("You trip on a memory sending you falling backwards through time... to before you were born")
print("\n")
print("Your stomach turns as you remember a familiar voice")
print("Something, possibly, from another lifetime. . .") # you are Van Helsing, reincarnated
quote1 = "'Listen to them, the children of the night. What music they make!' echoes in your mind" # no double ""
print(quote1)
print("You can't remember where it came from, but you know it is not a good thing at all")
print("The howling all around you is getting louder as you approach the deserted mansion")
print("Eerie flames line your path to the door as you spy 50 silvery eyes follow you from the treeline")
print("You are compelled to enter. . .")
print("\n")
print("...")
print("\n")
character_name = "Mina Harker" # string variable
character_age = 50
is_female = True
print("Inside the mansion. . .")
print("\n")
phrase = "mina harker's journal"
print(phrase.upper())
print(f"My name is { character_name }, and I am {character_age} years old") # concatenation string + integer
print("I'm looking for my husband, Jonathan.")
print("He has been missing for some time now.")
print("My gut is telling me that something lured him back to Transylvania.")
print("It has been 20 years since Van Helsing passed")
print("I'm afraid Jonathan and I are the only two left alive who know what happened so long ago")
print("I'm leaving tonight with to find him.")
print("\n")
count = 3

print("ENCOUNTER WITH COUNT VON COUNT")
counttoten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(counttoten)
friends = ["the count", "big bird", "cookie monster"]
print("AH AH AH AH AHHH!!")
print(friends)

def say_hi():
    print("Hi, friend.")
say_hi()

is_human= False
is_female= True

if is_female and is_human:
    print("You are a female human")
elif is_female and not is_human:
    print("You are a female creature")
elif not is_female and not is_human:
    print("You are a male creature")
else:
    print("You are a male human")
## Choose your Adventure interactive Haunted House -- 5 different forks in paths (choosing rooms)
# solve math problems to defeat monsters
print("\n")
print("Please store your name and age. . .")
print("\n")
your_name = input("Enter your name \n")
your_age = input("Enter your age \n")
print("\n")
is_female = True  # Boolean value
print("Hello, there, " + your_name + ". . . ")
print("\n")
print("You are walking through an old growth forest somewhere in the world.")
print("There is a chill in the night air")
print("The world is still except for the fog that swirls continuously around your feet")
print("Not even the smallest, most hidden crickets are chirping")
print("You come across a fork in your path.")
print("\n")
print("To the left is a clearing with thousands of pale, white moths fluttering above the brush")
print("To the right is a river. You hear its fresh water carrying off in the distance")
path_1=input("Will you go 1. left to the clearing, or 2. right to the river? \n")
if path_1 == 1: # you need two = signs for python conditionals
    print("bats swoop down all around you to catch the moths")
else:
    print("You hear beautiful music from below the water")
print("\n")
print("You have been walking through the woods all night now, and trip on something on the forest floor")
print("covered by the ferns and dirt, you see an old book")
print("you bend down and dust off the molding book. It reads 'Mina Harker's Journal'")
has_MinaHarkerjournal = input("Do you pick it up? \n")#if has_MinaHarkerjournal = True: she can use it to find secrets
print("You trip on a memory sending you falling backwards through time... to before you were born")
print("\n")
print("Your stomach turns as you remember a familiar voice")
print("Something, possibly, from another lifetime. . .") # you are Van Helsing, reincarnated
quote1 = "'Listen to them, the children of the night. What music they make!'" # no double ""
print(quote1)
print("The howling all around you is getting louder as you approach Dracula's mansion")
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
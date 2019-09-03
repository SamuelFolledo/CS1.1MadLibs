from termcolor import colored #in order to user termcolor library

def assign_input(name, gender, planet, noun, plural_pronoun, singular_pronoun, adjective, big_integer, flavor):
    male = [underlined("he"), underlined("He"), underlined("his"), underlined("His"), underlined("him"), underlined("himself")] #create a list of male pronounds
    female = [underlined("she"), underlined("She"), underlined("her"), underlined("Her"), underlined("her"), underlined("herself")] #create a list of female pronouns
    gender_list = male if gender == "m" or gender == "M" else female #if user inputted m for gender, then gender_list we will use will be male, otherwise, we will use our female list
    
    name = underlined(name)
    gender = underlined(gender)
    planet = underlined(planet)
    noun = underlined(noun)
    plural_pronoun = underlined(plural_pronoun)
    singular_pronoun = underlined(singular_pronoun)
    adjective = underlined(adjective)
    big_integer = underlined(big_integer)
    flavor = underlined(flavor)

    #paragraph 1
    print("Once upon a time in planet " + planet + ", lived a daring 5 years old "+ noun +" named "+name+". For one weekend, "+name+" together with "+gender_list[2]+" lovely mother, father, and two sibings were invited to a huge gathering in a medium sized resort consisted of close friends, families, and some random "+plural_pronoun+". This resort had two "+adjective+" swimming pools: a pool for young "+noun+"s that is zero to two feet deep, and another pool for the taller and much older "+noun+"s that begins from 4 feet all the way up to "+str(big_integer)+" feet deep. "+name+" not usually having many chances to swim in a swimming pool, had lots of fun with other young "+noun+"s playing tag. A few hours later as the night approached, "+name+" looked to "+gender_list[2]+" left at the other swimming pool and saw how the older "+noun+"s were having so much fun. "+gender_list[1]+" thought to himself, why not me? So "+name+" tipped toe past the gazebo full of people and sneakily made "+gender_list[2]+" way to the steps of the swimming pools. "+name+" carefuly took one step at a time while holding on tightly the wall of the pool. With a huge grin on "+gender_list[2]+" face, "+gender_list[0]+" reached the last step of the pool where the water only reached all the way up to "+gender_list[2]+" chest. Curious on how deep the last step was, "+gender_list[0]+" took one last step, which "+gender_list[0]+" found out was the tallest step and immediately sank, and had the water level just right above "+gender_list[2]+" eye level. "+gender_list[1]+" tried to grab the edge but it was too far, "+gender_list[0]+" tried to retrack "+gender_list[2]+" steps, but it was too far and high. Lastly, "+gender_list[0]+" tried to jump up to scream for help, but noone can hear him because "+gender_list[2]+" mouth was right underneath the water. Jumping could only do so little as water still flows down from "+gender_list[2]+" hair down to "+gender_list[2]+" face, removing "+gender_list[2]+" ability to breathe through "+gender_list[2]+" nose. "+gender_list[1]+" was however in peace to see everyone having fun, laughing, as the round-shaped light of the lamp turned into diamond then into a straight line. Is this the end for the daring and energetic "+noun+" from planet "+planet+"?")
        #Remember to convert int to string when adding it to a string
    #paragraph 2
    a_an = a_or_an(singular_pronoun) #call the a_or_an method to decide if our object will either be a or an depending on singular_pronoun's first character
    print("A couple of minutes later, "+a_an+" "+singular_pronoun+" saw and decided to join the fun with other older "+noun+"s in the swimming pool. As he walks down the stairs of the pool, he stepped on a little "+noun+" who fully sank underneath the pool. Not knowing or caring who it was, he immediately took the "+noun+" out of the pool and alerted everyone that someone drowned. Everyone had a curious and worried face and immediately rushed in to see who it was. They saw a young "+noun+" with a huge belly from all the water inhaled, purple from head to toe, and worst of all, with no heartbeat. The father accompanied by a closed friend, immediately rushed to give his son a CPR. Not caring about the current repercussion and taste of the pool water mixed with a slightly "+flavor+" flavor from the inside of a dead "+noun+", the father kept pumping and giving all his oxygen to his dead son. A couple of water removed and minutes passed, yet still no breathe nor heartbeat, but only discharges of waste from his rear bottom. After some prayers and cries from the observing concerned families and "+plural_pronoun+", the young "+noun+" coughed out the remaining water inside "+gender_list[2]+" body. Still unconscious but this time, "+gender_list[0]+" was breathing and there was a heartbeat.")
    #paragraph 3
    print("The next morning, "+name+" found "+gender_list[5]+" in a new place, everything was mostly white, it was a hospital "+gender_list[0]+" slept at for the night. After a breakfast, "+gender_list[0]+" returned to the resort with the father. As "+gender_list[0]+" greeted everyone, "+gender_list[0]+" noticed all eyes were glued on "+gender_list[4]+". Everyone looked at "+gender_list[4]+" differently, as "+gender_list[0]+" did looked different. This little five years old "+noun+" went face to face and was victorious against a battle noone in the gathering has ever fought before nor dares to confront. "+gender_list[1]+" served as an insipration to everyone, that if "+gender_list[0]+" can overcome death itself at such a young age, anyone can get through any problematic obstacles as well. "+gender_list[1]+" raised many eyebrows on what else is "+gender_list[0]+" meant to do? What else has God planned for "+gender_list[4]+"? That is too incomprehensible to know. However, there is one thing "+name+" knows for sure, it is that "+gender_list[0]+" is meant to soar above any challenges "+gender_list[0]+" comes across. Now "+name+" is a current student at Make School who has a goal to not simply get a degree, but to initialize a positive wave and dominate. To lead and be the best possible example for anyone "+gender_list[0]+" comes in contact with. Most importantly, to be unfazed and abide to what "+gender_list[0]+" believes is right. "+gender_list[3]+" curiousity will take him far, but "+gender_list[2]+" imagination and positive attitude will take "+gender_list[4]+" further.")

def underlined(word): #method that bolds and underlines any given word; used for all inputs in the story
    return colored(str(word), attrs=['bold', 'underline'])

def a_or_an(word): #method that grabs a word and return "an" if the first letter of the word is a vowel
    return "an" if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o"  or word[0] == "u" else "a"

def user_int_input(prompt): #for INT user input
    user_input = input((colored(prompt, "cyan"))) #grabs user input 
    while user_input.isdigit() == False: #ensures the input is an integer
        user_input = input(colored("Please enter a whole number only: ","red", attrs=['bold'])) #ask for user input again
    return int(user_input) #return the user_input as an integer

def user_input(prompt): #this method will display a message in the terminal and wait for user input
    user_input = input((colored(prompt, "cyan"))) #user_input will equal to what the user inputted in a string format
    # while user_input == "" or user_input == " ": #ensures that the user does input a value and not just a blank or space
    while any(char.isdigit() or char.isspace() for char in user_input): #while any character in user_input has digit or space, ask the user to change the input
        user_input = input(colored("Please enter letters only: ", "red", attrs=['bold'])) #ask for the input again
    return user_input #return the user input as a string

def start():
    print("\n\n")
    print (colored("-----------------------------------------Welcome to Samuel Folledo's MadLibs-----------------------------------------", "blue", "on_white", attrs=['bold', 'underline']))
    name = user_input("Enter the name of the main character: ")
    gender = user_input("Enter the gender(m/f) of the main character: ") #ask for user to input a gender which can only be m or f
    while gender != "f" and gender != "F" and gender != "m" and gender != "M": #use and gate instead of or gate to ensure user can only pick m/f
        gender = user_input("Please enter m for male, and f for female: ") # basically forces users to only input m or f
    planet = user_input("Enter a name of a planet: ")
    noun = user_input("Enter a singular noun: ")
    plural_pronoun = user_input("Enter a plural pronoun: ")
    singular_pronoun = user_input("Enter a singular pronoun: ")
    adjective = user_input("Enter an adjective: ")
    big_integer = user_int_input("Enter a big integer (>5): ")
    while big_integer <= 5: #forces user to input an integer greater than 5 only
        big_integer = user_int_input(colored("Enter a whole integer greater than 5: ", "red", attrs=['bold']))
    flavor = user_input("Enter a flavor: ")

    assign_input(name, gender, planet, noun, plural_pronoun, singular_pronoun, adjective, big_integer, flavor) #call our assign_input method and inputting our user inputs in the parameter 



start() #execute our code











"""
planet = Earth
noun1 = kid
name1 = Samuel
he/she = male
him/her = him
his/her = his
himself/herself = male
pronoun1(plural) = church friends/people
pronoun2(singular) = angel/savior
adjective1 = huge/clear/beautiful
big integer = 6
flavor = icky

------------------------------ SHORT STORY ---------------------------------------
"""





def assign_input(name, gender, planet, noun, plural_pronoun, singular_pronoun, adjective, big_integer, flavor):
    male = ["he", "He", "his", "His", "him", "himself"] #create a list of male pronounds
    female = ["she", "She", "her". "Her", "her", "herself"] #create a list of female pronouns
    gender_list = male if gender == "m" or gender == "M" else female #if user inputted m for gender, then gender_list we will use will be male, otherwise, we will use our female list
    # he_she = "he" if gender == "m" or gender == "M" else "she"
    # big_he_she = "He" if gender == "m" or gender == "M" else "She"
    # him_her = "him" if gender == "m" or gender == "M" else "her"
    # his_her = "his" if gender == "m" or gender == "M" else "her"
    # big_his_her = "His" if gender == "m" or gender == "M" else "Her"
    # himself_herself = "himself" if gender == "m" or gender == "M" else "herself" 

    #paragraph 1
    print("Once upon a time in planet " + planet + ", lived a daring 5 years old "+ noun +" named "+name+". For one weekend, "+name+" together with "+gender_list[2]+" lovely mother, father, and two sibings were invited to a huge gathering in a medium sized resort consisted of close friends, families, and some random "+plural_pronoun+". This resort had two "+adjective+" swimming pools: one for young "+noun+"s that is zero to two feet deep, and another pool for the taller and much older "+noun+"s that begins from 4 feet all the way up to "+str(big_integer)+" feet deep. "+name+" not usually having many chances to swim in a swimming pool, had lots of fun with other young "+noun+"s playing tag. A few hours later as the night approached, "+name+" looked to "+gender_list[2]+" left at the other swimming pool and saw how the older "+noun+"s were having so much fun. "+gender_list[1]+" thought to himself, why not me? So "+name+" tipped toe past the gazebo full of people and sneakily made "+gender_list[2]+" way to the steps of the swimming pools. "+name+" carefuly took one step at a time while holding on tightly the wall of the pool. With a huge grin on "+gender_list[2]+" face, "+gender_list[0]+" reached the last step of the pool where the water only reached all the way up to "+gender_list[2]+" chest. Curious on how deep the last step was, "+gender_list[0]+" took one last step, which "+gender_list[0]+" found out was the tallest step and immediately sank, and had the water level just right above "+gender_list[2]+" eye level. "+gender_list[1]+" tried to grab the edge but it was too far, "+gender_list[0]+" tried to retrack "+gender_list[2]+" steps, but it was too far and high. Lastly, "+gender_list[0]+" tried to jump up to scream for help, but noone can hear him because "+gender_list[2]+" mouth was right underneath the water. Jumping could only do so little as water still flows down from "+gender_list[2]+" hair down to "+gender_list[2]+" face, removing "+gender_list[2]+" ability to breathe through "+gender_list[2]+" nose. "+gender_list[1]+" was however in peace to see everyone having fun, laughing, as the round-shaped light of the lamp turned into diamond then into a straight line. Is this the end for the daring and energetic "+noun+" from planet "+planet+"?")
        #Remember to convert int to string when adding it to a string

    #paragraph 2
    print("A couple of minutes later, a "+singular_pronoun+" saw and decided to join the fun with other older "+noun+"s in the swimming pool. As he walks down the stairs of the pool, he stepped on a little "+noun+" who fully sank underneath the pool. Not knowing or caring who it was, he immediately took the "+noun+" out of the pool and alerted everyone that someone drowned. Everyone had a curious and worried face and immediately rushed in to see who it was. They saw a young "+noun+" with a huge belly from all the water inhaled, purple from head to toe, and worst of all, with no heartbeat. The father accompanied by a closed friend, immediately rushed to give his son a CPR. Not caring about the current repercussion and taste of the pool water mixed with a slightly "+flavor+" flavor from the inside of a dead "+noun+", the father kept pumping and giving all his oxygen to his dead son. A couple of water removed and minutes passed, yet still no breathe nor heartbeat, but only discharges of waste from his rear bottom. After some prayers and cries from the observing concerned families and "+plural_pronoun+", the young "+noun+" coughed out the remaining water inside "+gender_list[2]+" body. Still unconscious but this time, "+gender_list[0]+" was breathing and there was a heartbeat.")

    #paragraph 3
    print("The next morning, "+name+" found "+gender_list[5]+" in a new place, everything was mostly white, it was a hospital "+gender_list[0]+" slept at for the night. After a breakfast, "+gender_list[0]+" returned to the resort with the father. As "+gender_list[0]+" greeted everyone, "+gender_list[0]+" noticed all eyes were glued on "+gender_list[4]+". Everyone looked at "+gender_list[4]+" differently, as "+gender_list[0]+" did looked different. This little five years old "+noun+" went face to face and was victorious against a battle noone in the gathering has ever fought before nor dares to confront. "+gender_list[1]+" served as an insipration to everyone, that if "+gender_list[0]+" can overcome death itself at such a young age, anyone can get through any obstacles as well. "+gender_list[1]+" raised many eyebrows on what else is "+gender_list[0]+" meant to do? What else has God planned for "+gender_list[4]+"? That is too incomprehensible to know. However, there is one thing "+name+" knows for sure, it is that "+gender_list[0]+" is meant to soar above any challenges "+gender_list[0]+" comes across. Now "+name+" is a current student at Make School who has a goal to not simply get a degree, but to initialize a positive wave and dominate. To lead and be the best possible example for anyone "+gender_list[0]+" comes in contact with. Most importantly, to be unfazed and abide to what "+gender_list[0]+" believes is right. "+gender_list[3]+" curiousity will take him far, but "+gender_list[2]+" imagination and positive attitude will take "+gender_list[4]+" further.")


def user_int_input(prompt): #for INT user input
    user_input = int(input(prompt))
    return user_input

def user_input(prompt): #this method will display a message in the terminal and wait for user input
    user_input = input(prompt) #user_input will equal to what the user inputted
    return user_input

def start():
    print("--------------------------------------Welcome to Samuel Folledo's MadLibs--------------------------------------")
    name = user_input("Enter the name of the main character: ")

    gender = user_input("Enter the gender(m/f) of the main character: ")
    while gender != "w" and gender != "W" and gender != "m" and gender != "M": #use and gate instead of or gate to ensure user can only pick m/f
        gender = user_input("Please enter m for male, and f for female: ")

    planet = user_input("Enter a name of a planet: ")
    noun = user_input("Enter a noun: ")
    plural_pronoun = user_input("Enter a plural pronoun: ")
    singular_pronoun = user_input("Enter a singular pronoun: ")
    adjective = user_input("Enter an adjective: ")
    big_integer = user_int_input("Enter a big integer: ")
    flavor = user_input("Enter a flavor: ")

    assign_input(name, gender, planet, noun, plural_pronoun, singular_pronoun, adjective, big_integer, flavor)    



start()











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



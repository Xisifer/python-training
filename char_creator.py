import inquirer
import random
from char_properties import Character
from char_creation_menus import *
# from char_creation_rollers import *

from char_creation_rollers import roll_race
from char_creation_rollers import roll_homeland
from char_creation_rollers import roll_origin
from char_creation_rollers import roll_family_fate
from char_creation_rollers import roll_parents
from char_creation_rollers import roll_life_events


# def bare_text(string):
#     print(f'bare string is {string}')
#     strip1 = string.strip('[]') # remove [dictionary brackets]
#     strip2 = strip1.strip('\"') # remove "double quotes"
#     stripped_text = strip2.strip("\'") # remove 'single quotes'
#     return stripped_text



def flip():
    if random.randint(0,1):
        return 0
    else:
        return 1



def name_input():
    char_name = input("Do you want to roll dice? Y/N ")
    name_stripped = str(char_name.strip())
    print(f'You said: {name_stripped}')


def store_data(category, selection):
    # print(f'Saving {selection} into character {category}...')
    Character.category = selection


    match category:
        case 'race': 
            Character.race = selection
            print(f'Data saved. Character\'s {category} is now {Character.race}')        
        case 'home': 
            Character.home = selection
            print(f'Data saved. Character\'s {category} is now {Character.home}')       
        case 'origin':
            Character.origin = selection
            print(f'Data saved. Character\'s {category} is now {Character.origin}')
        case 'age':
            Character.age = selection
            print(f'Data saved. Character\'s {category} is now {Character.age}')
        case 'family':
            Character.family = selection
            print(f'Data saved. Character\'s {category} is now {Character.family}')       
        case 'parents':
            Character.family = selection
            print(f'Data saved. Character\'s {category} is now {Character.family}')
        case _: 
            Character.category = selection
            print(f'Character.category is {selection}')

def check_saved_data():
    print('Total saved character data so far: ')

    if __name__ == '__main__':
        temp = vars(Character)
        for item in temp:
            if not item.startswith('__'):
                if not item.startswith('category'):
                    print(item , ' : ' , temp[item])




def ask_reroll(question_text, roll_result):
    choice_menu = {
        inquirer.List('menu',
                    message=f'{question_text} {roll_result}',
                    choices=['Accept', 'Reroll'], default=['Accept']
        )
    }
    answer = inquirer.prompt(choice_menu)

    if answer['menu'] == 'Reroll':
        print("Rerolling...")
        return True
    else:
        print("Moving on...")
        return False
    

def char_question(q_text, roll_choice, category, insert_data): 




    # is_tuple = 

    if type(insert_data) is tuple:
        # print(f'The tuple is {len(insert_data)} items long.')
        i=0
        while i < len(insert_data):
            print(insert_data[i])
            i=i+1
        # print(f'first data of tuple {insert_data} is {insert_data[0]}.')
        insert_data = insert_data[0]
        # print(f'insert_data[0] is: {insert_data}')
    else:
        insert_data = insert_data
        # print(f'insert_data is: {insert_data}')

    retry = True
    while retry :
        
        question_text = q_text
        
        question_result_tuple = roll_choice(insert_data)
        question_result = question_result_tuple[0]
        
        # print(f'==========\nDEBUG\n==========')
        # print(f'question_result is: {question_result}')
        
        # print(f'Beginning char_question')
        # print(f'roll_choice is: {roll_choice}')
        # print(f'category is: {category}')
        # print(f'insert_data is: {insert_data}')
        # print(f'==========\nEND DEBUG\n==========')
        retry = ask_reroll(question_text, question_result)
    store_data(category, question_result)
    return question_result

def char_creation():

    # question 1: Race
    print(f'============\nQUESTION 1\n============')
    race_result = char_question('Choose race:', roll_race, 'race', '')
    
    # question 2: Homeland
    print(f'============\nQUESTION 2\n============')
    char_home = char_question('Your homeland:', roll_homeland, 'home', race_result)

    # question 3: Origin
    print(f'============\nQUESTION 3\n============')
    # packing up Q1 & Q2 into a tuple
    char_data = (race_result, char_home)
    print(f'Beginning Question 3 with char_data: {char_data}')
    char_question('Your character is from:', roll_origin, 'origin', char_data)


    # question 4: Family status
    print(f'============\nQUESTION 4\n============')
    char_question('Your character\'s family:', roll_family_fate, 'family', race_result)

    # question 5: Parents status
    print(f'============\nQUESTION 5\n============')
    print(f'inserting race_result {race_result} into roll_parents')
    char_question('Your character\'s parents:', roll_parents, 'parents', race_result)

    # question 6: Life Path
    print(f'============\nQUESTION 6\n============')
    print('This RPG assumes a major noteworthy event happened to you every 5 years.')

    while True:
        try:
            char_age = input('How old is your character? (20 - 100)')
            if char_age.isdigit():
                char_age = int(char_age)
            else:
                raise ValueError()
            if 20 <= char_age <= 100:
                break
            raise ValueError()
        except ValueError:
            print('Please enter a number between 20 and 100.')


    age = 0
    life_milestones = []
    for age in range(5, char_age, 5):
        life_milestones.append(age)

    life_events_num = len(life_milestones)

    print(f'You are {char_age} years old. This means you had {life_events_num} big Life Path events.')
    print(f'You have had major life events at ages {life_milestones}')
    category = 'age'
    store_data(category, char_age)


    # question 7

    # retry = True
    # while retry :
    question_text = 'Major Life Events'
    char_life_events = roll_life_events(race_result, char_age, life_milestones)
    # retry = ask_reroll(question_text, char_life_events) 
    category = 'life events'
    store_data(category, char_life_events) 





# ==================
# = CREATION START =
# ==================
char_creation()




# ================================================
#  Example of working "pause for user input" code
# ================================================

# player_answer = input("Do you want to roll dice? Y/N ")
# answer_stripped = str(player_answer.strip())
# print(f'You said: {answer_stripped}')

# if answer_stripped == "Y" or answer_stripped == "y": 
#     roll_results = []

#     print("Rolling 1d10...")
#     roll = random.randint(1,10)
#     roll_results.append(roll)

#     print(f'Result: {str(roll_results)}')

# else:
#     print("Dice roll cancelled.")

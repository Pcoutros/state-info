'''This a python command line menu-driven application that allows a user to
display the state capital, population, and flower of each state, search for a
state to display its information and a picture of its flower, create a bar
graph of the top 5 populations, and update a states population. The application
continues until the 'End Program' option is selected.

State information comes from a text file - states.txt
flower pictures come from a folder - flowers

*TO RUN THIS PROGRAM, THIS .PY FILE, THE STATES.TXT FILE, AND THE FLOWERS 
FOLDER NEED TO BE IN THE SAME FOLDER.

Name: Pete Coutros
Course: SDEV 300 7380
Date: 03/31/2023'''

# Imports
import sys
from operator import itemgetter
import matplotlib.pyplot as plt
from PIL import Image

# Read in text file to list of lists containing states and respective info
with open('states.txt', encoding='utf-8') as file:

    # Initialize blank list
    states = []

    # Add each state and its respective info into the list
    for state_info in file:
        states.append(state_info.strip().split(','))


# Define display states function
def display_states():

    '''This function displays all states and their respective info

    It loops through the states list to display the info.
    Input: None
    Output: None
    '''

    # Sort states to be printed in alphabetical order
    states.sort()

    # Display heading info for columns
    print(f"\n{'State':<18}{'Capitol':<18}{'Population':<15}{'Flower':<15}")
    print(f"{'-'*5:<18}{'-'*7:<18}{'-'*10:<15}{'-'*6:<15}\n")

    # Loop through all states to print individual state info
    for state in states:
        pop = f"{int(state[2]):,}"  # Format commas
        print(f"{state[0]:<18}{state[1]:<18}{pop:<15}{state[3]:<15}")


# Define search function
def search():

    '''This function will prompt the user for a state and validate it.

    the input is searched in the state lists for a match.
    Input: None
    Output: list of searched state characteristics'''

    # Initialize loop control variable
    is_valid = False

    # Validate user input
    while not is_valid:

        # Prompt user for input and strip
        selected_state = input('Please enter the state you want to look up:'
                               '\t').strip()

        # Loop through states to find a match from the user input
        for state in states:

            # If input exists in states list, display state info
            if selected_state.upper() == state[0].upper():

                found = state[:]
                is_valid = True

        # Display error on invalid input
        if is_valid is False:
            print('Invalid input.')

    return found


# Define search states function
def dispaly_a_state(state):

    '''This function displays a state using input from the search function.

    It displays the state info to the user and shows an image of the flower.
    Input: List of searched state characteristics
    Output: None'''

    # Display state info
    print(f"\n{'State':<18}{'Capitol':<18}{'Population':<15}"
          f"{'Flower':<15}")
    print(f"{'-'*5:<18}{'-'*7:<18}{'-'*10:<15}{'-'*6:<15}\n")
    pop = f"{int(state[2]):,}"  # Format commas
    print(f"{state[0]:<18}{state[1]:<18}{pop:<15}{state[3]:<15}")

    # Open and display image of flower
    img = Image.open('flowers/' + state[4])
    img.show()


# Define bar graph function
def bar_graph():

    '''This function will display a bar graph of the top 5 populations.

    The X axis is the state name and the Y axis is the population.
    Input: None
    Output: None'''

    # Initialize dictionary for key=state value=population
    state_pop = {}

    # Loop through states and add states and populations to dictionary
    for state in states:
        state_pop[state[0]] = int(state[2])

    # Sort and make dictionary of top 5
    top5 = dict(sorted(state_pop.items(), key=itemgetter(1), reverse=True)[:5])

    # Create bar graph
    plt.bar(top5.keys(), top5.values())

    # Format bar graph
    plt.title('Top 5 Populated States')
    plt.xlabel('State Names')
    plt.ylabel('Population')

    # Display bar graph
    plt.show()


# Define update state population function
def update_states(state):

    '''This function allows the user to update a state's population.

    The user selects the state and enters a new integer.
    Input: List of searched state characteristics
    Output: None'''

    # Validate user input
    while True:

        # Prompt user for new population and try int conversion
        try:
            population = int(input('Please enter the updated population:\t'))

            # Validate non-negative entry
            if population >= 0:

                # Remove, update, replace list back in states
                states.remove(state)
                state[2] = str(population)
                states.append(state)
                states.sort()

                # Display confirmation of the change
                print(f"\nThe population of {state[0]} was successfully "
                      f"updated to {int(state[2]):,}.")

                break

            print('Population must be non-negative.')

        # Except invalid population input and display error message
        except ValueError:
            print('Invalid input.')


# Define menu options function
def menu_options():

    '''This function will display the menu options.

    It features 5 items to choose from.
    Input: None
    Output: None'''

    # Display menu options
    print('\nPlease choose from the menu options below:\n'
          '\n1.\tDisplay all U.S. States in Alphabetical order along with the '
          'Capital, State Population, and Flower.'
          '\n2.\tSearch for a specific state and display the appropriate '
          'Capital, State Population, and an image of the associated State '
          'Flower.'
          '\n3.\tProvide a Bar graph of the top 5 populated States showing '
          'their overall population.'
          '\n4.\tUpdate the overall state population for a specific state.'
          '\n5.\tExit Program.\n')


# Define process menu selection function
def process_selection(user_selection):

    '''This function will process the menu option selected.

    Input: User selection
    Output: None'''

    # If selection 1 proceed with display function
    if user_selection == 1:
        print('')
        display_states()

    # If selection 2 proceed with search function
    elif user_selection == 2:
        state = search()
        dispaly_a_state(state)

    # If selection 3 proceed with bar graph function
    elif user_selection == 3:
        bar_graph()

    # If selection 4 proceed with update function
    elif user_selection == 4:
        state = search()
        update_states(state)

    # If selection 'f' thank user and end program
    elif user_selection == 5:
        print('Thank you for using this program, have a great day!')
        sys.exit()

    else:
        print('Invalid input.')


# Define main function of program
def main():

    '''This is the main function of the program.

    It will be called to execute the program.'''

    # Display welcome message
    print('Welcome to the State Information Application! Use the menu below '
          'to navigate through the application.')

    # Initiate loop control variable
    is_valid = True

    # Validate user input
    while is_valid:

        # Display menu options
        menu_options()

        # Prompt user for menu selection and try to convert to int
        try:
            selection = int(input('Please enter your selection:\t'))

            # Process user selection
            process_selection(selection)

            # If '5' is selected exit loop
            if selection == 5:
                is_valid = False

        # Ecept invalid inputs
        except ValueError:
            print('Invalid input.')


# Execute---------------------------------------------------------------------
main()

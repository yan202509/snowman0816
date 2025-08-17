SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]


def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratulations, you win!'
    If the player wins and, 
    'Sorry, you lose! The word was {snowman_word}' if the player loses
    """


    # the correct list is from the helper function build_letter_status_dict
    # the parameter of snowman_word is from a random generation, which is the word we working on
    # this is correct because the user input a letter that match with any letter in the word
    # the word is snowman_word
    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
    wrong_guesses_list = []

    while len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES:
        user_input = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)
        # Use the new variable snowman_word instead of the constant variable SNOWMAN_WORD here:
        # this is hint 4 in 'Using the Letter Status Dictionary'
        if user_input in correct_letter_guess_statuses:
            print("You guessed a letter that's in the word!")
            correct_letter_guess_statuses[user_input] = True
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)

        # this print_snowman is from the helper function below at line 123
        print_snowman_graphic(len(wrong_guesses_list))
        print(f"Wrong guesses:{wrong_guesses_list}")

        # call the helper function, means to actually use it here in the main function
        # if we do not use it here, the function is not being used at all
        # print the string either correct or not 

        # just displaying the _ _ _ or the letter that's correct
        print_word_progress_string(snowman_word, correct_letter_guess_statuses)

        # if every letter is guessed, means completed the game of guessing
        # the else function is outside of if, because when chances are not used up
        # the game will continue to loop over this while function
        if is_word_guessed(snowman_word, correct_letter_guess_statuses):
            print("Congratulations, you win!")
            return
        
    # or when use up the chances, the game ends
    else:
        # print("Sorry, you lose! The word was {snowman_word}")
        print(f"Sorry, you lose! The word was {snowman_word}")


def print_snowman_graphic(wrong_guesses_count):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """
    
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """

    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_statuses       
                and correct_letter_guess_statuses[user_input_string]): 
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string
    

def build_letter_status_dict(snowman_word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """

    letter_status_dict = {}
    for letter in snowman_word:
        letter_status_dict[letter] = False
    return  letter_status_dict
    

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It calls another function to generate a string representation of the  
    user's progress towards guessing snowman_word and prints this string.
    """

    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)


def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It creates and returns an output string that shows the correct letter 
    guess placements as well as the placements for the letters yet to be 
    guessed.
    """

    output_string = ""
    is_not_first_letter = False

    for letter in snowman_word:
        if is_not_first_letter:
            output_string += " "

        if correct_letter_guess_statuses[letter]:
            output_string += letter
        else:
            output_string += "_"

        is_not_first_letter = True

    return output_string


def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """

    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True
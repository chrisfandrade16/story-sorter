# Opening the input file
short_story_file = open('ShortStory.txt', 'r')

# Reading and locally storing contents of the input file
short_story_text = short_story_file.read()
short_story_text_length = len(short_story_text)

# Closing the input file
short_story_file.close()

# ASCII standard decimal values for the characters "A" and "Z"
A_ascii_decimal = 65
Z_ascii_decimal = 90

# ASCII standard decimal values for the characters "a" and "z"
a_ascii_decimal = 97
z_ascii_decimal = 122

# A dictionary (mapping key to value) that stores the uppercase letters of the alphabet
# as keys, and an array of the sentneces that start with those letters as values
first_letter_to_sentences_dictionary = {}

# Initializing the dictionary by looping through the ASCII decimal
# values of A to Z for the keys, and an initial empty array for the values
for character_decimal in range(A_ascii_decimal, Z_ascii_decimal + 1):
    character_string = chr(character_decimal)
    first_letter_to_sentences_dictionary[character_string] = []

# This flag represents the status as we approach the end of a sentence:
#
# -1: We are currently inside a quote (all other flags mean we
#     are currently outside a quote)
#  0: We are in the middle of a sentence
#  1: We have hit a punctuation or ending quotation mark possibly indicating
#     the end of a sentence is approaching (if the flag is 0)
#  2: We have hit a space or newline character possibly indicating the
#     next character will be a different sentence
#  
# If that next character is a capial letter or a starting quotaiton mark, we
# know that we've ended the sentence and entered a new one
ending_sentence_flag = 0

# This stores the current sentence we are attempting to isolate
current_sentence = ""

# This stores the current first letter of that current sentence
current_first_letter = None

# This stores the current character index among the whole story we are analyzing
character_index = 0

# Going through each character in the story, thus the time complexity of
# this algorithm should be O(n), where n is the number of characters in the story
while character_index < short_story_text_length:
    # Calculating the character string and character ASCII decimal from the character index
    character_string = short_story_text[character_index]
    character_decimal = ord(character_string)

    # These are booleans to check if the current character is of a certain type
    character_is_lowercase_letter = character_decimal >= a_ascii_decimal and character_decimal <= z_ascii_decimal
    character_is_uppercase_letter = character_decimal >= A_ascii_decimal and character_decimal <= Z_ascii_decimal
    character_is_quote = character_string == '"'
    character_is_start_quote = character_is_quote and ending_sentence_flag == 0
    character_is_end_quote = character_is_quote and ending_sentence_flag == -1
    character_is_punctuation = character_string == '?' or character_string == '!' or character_string == '.' or character_string == ":"
    charcter_is_space = character_string == ' '
    charcter_is_newline = character_string == '\n'

    # Adding the current character to the current sentence string
    current_sentence += character_string

    # If there is no first letter assigned and it is an uppercase letter, mark
    # it as the current first letter of the current sentence
    if current_first_letter == None and character_is_uppercase_letter:
        current_first_letter = character_string

    # If we have reached the end of the story, which might not have a standardized
    # character ending, mark it as the end of the current sentence anyways and
    # store it in the dictionary
    if character_index == short_story_text_length - 1:
        first_letter_to_sentences_dictionary[current_first_letter].append(current_sentence)
        break

    if character_is_start_quote:
        # If the character is the start of a quotation, make the flag -1
        ending_sentence_flag = -1
    elif character_is_end_quote:
        # Once the quote has ended, return the flag to 0
        ending_sentence_flag = 0

    # Only check for the end of a sentence if we are not in a quote
    if ending_sentence_flag != -1:
        if character_is_lowercase_letter:
            # If the current character is a lowercase letter, we are still in the middle of a
            # a sentence, so set the flag to 0
            ending_sentence_flag = 0
        elif (character_is_punctuation or character_is_quote) and ending_sentence_flag == 0:
            # If the current character is a punctuation or a quotation mark, we may be near the
            # end of a sentence, so keep track of this through setting the flag as 1
            ending_sentence_flag = 1
        elif (charcter_is_space or charcter_is_newline) and ending_sentence_flag == 1:
            # If the current character is now a space or a newline, this may indicate that the
            # next character will be a new sentnece, so set the flag as 2
            ending_sentence_flag = 2
        elif (character_is_uppercase_letter or character_is_quote) and ending_sentence_flag == 2:
            # If the current character is now an uppercase letter or another quotation
            # mark, this means we are now in a new sentence

            # Let's add the current sentence to the dictionary at the slot of the current 
            # sentence's first letter, making sure to not use the last character, since it
            # belongs to the next sentence
            first_letter_to_sentences_dictionary[current_first_letter].append(current_sentence[:-1])

            # Reset the flags and go back one character to reanalyze this character
            # since it belongs to the next sentence
            ending_sentence_flag = 0
            current_first_letter = None
            current_sentence = ""    
            character_index -= 1
    
    # Move to the next character
    character_index += 1

# Opening the ouput file
short_story_rearranged_file = open("ShortStoryRearranged.txt", "w")

# Going through each first letter alphabetically (A-Z)
# and pasting it into the output file
for first_letter_decimal in range(A_ascii_decimal, Z_ascii_decimal + 1):
    first_letter_string = chr(first_letter_decimal)
    sentences_with_first_letter = first_letter_to_sentences_dictionary[first_letter_string]

    for sentence in sentences_with_first_letter:
        if(sentence[-1] != '\n'):
            # If last letter is not a newline, add a newline so that the alphabetical sorting of the
            # sentences is easily visible in the output file
            sentence += '\n'

        short_story_rearranged_file.write(sentence)

# Closing the output file
short_story_rearranged_file.close()

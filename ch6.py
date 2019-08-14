def chars_in_camus():
    """
    :return: str "Camus"
    """
    return "Camus"


# for char in chars_in_camus():
#     print(char)

def multi_input_string(str1, str2):
    """
    :param str1: str
    :param str2: str
    :return: str
    """
    return "Yesterday I wrote a {}. I sent it to {}!".format(str1, str2)


# string_one = input('Give me a noun describing a type of writing: ')
# string_two = input('Give me a proper noun representing a person: ')
# string_two = string_two.split()
# print(multi_input_string(string_one.lower(), ' '.join(s.capitalize() for s in string_two)))

def capitalize_string(string):
    """
    :param string: str
    :return: str with the first letter capitalized
    """
    temp_string = string
    if string[0].islower():
        temp_string = string[0].upper() + string[1:]
    return temp_string


# print(capitalize_string('aldous Huxley was born in 1894.'))

def split_on_question_mark(string_to_split):
    """
    :param string_to_split: str
    :return: str split on space and item joined in pairs
    """
    sts_iter = iter(string_to_split.split(" "))
    return [item + ' ' + next(sts_iter, '') for item in sts_iter]


# print(split_on_question_mark('Where now? Who now? When now?'))

def create_sentence_from_strings(list_of_strings):
    """
    :param list_of_strings: list of str
    :return: string of strings joined on blank space
    """
    return " ".join(list_of_strings).replace(" .", ".")


# def strip_space_before_period(list_of_strings):
#     """
#     :param list_of_strings: list of str
#     :return: string with
#     """
#     string_with_blank = create_sentence_from_strings(list_of_strings)
#     # location_of_blank = string_with_blank.index(' .')
#     # return string_with_blank[:location_of_blank] + string_with_blank[location_of_blank+1:]
#     return string_with_blank.replace(" .", ".")


# print(strip_space_before_period(["The", "fox", "jumped", "over", "the", "fence", "."]))

# print(create_sentence_from_strings(["The", "fox", "jumped", "over", "the", "fence", "."]))

def replace_s_with_dollar_sign(string_to_modify):
    """
    :param string_to_modify: str
    :return: str with all instances of 's' replaced with '$'
    """
    return string_to_modify.replace('s', '$')


# print(replace_s_with_dollar_sign("A screaming comes across the sky."))

def index_of_first_m(string_to_search):
    """
    :param string_to_search: str
    :return: int of the index of the first instance of the letter 'm'
    """
    return string_to_search.index('m')


# print(index_of_first_m('Hemingway'))

def three_times_three(string_to_repeat):
    """
    :param string_to_repeat: str
    :return: a string repeated three times via concatenation and the same string repeated three times by multiplication
    """
    return string_to_repeat + ' ' + string_to_repeat + ' ' + string_to_repeat + '\n' + \
           ((string_to_repeat + ' ') * 3).strip()


# print(three_times_three('three'))

def slice_a_string(string_to_slice, char_to_slice_before):
    """
    :param string_to_slice: str
    :param char_to_slice_before: str
    :return: str sliced to the character denoted by the second parameter
    """
    return string_to_slice[:string_to_slice.index(char_to_slice_before)]


# print(slice_a_string('It was a bright cold day in April, and the clocks were striking thirteen.', ','))

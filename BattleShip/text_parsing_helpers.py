"""

non class helper functions, could have moved them into another file

"""

def remove_comments_and_whitespace(input_str: str):
    """
    :param input_str:
    :return: a string that has all the comments from the input file removed.
    """
    return input_str.replace(" ","").split('//')[0]

def parse_initial_states_text_into_args_list(text: str):
    """
    :param text: text
    :return: list of arguments in text format
    """

    text = text.rstrip().replace(")(", ",")  # for any newlines
    text = text.replace("(", "").replace(")", "").replace(" ", "")  # tried regex but was getting a bit complex
    return list(text.split(','))

def group_list_arguments_by_3(list_input: list):
    """
    :param list_input: list of strings
    :return sub_lists: list a list of lists where each sub list if of size 3
    """
    N = 3
    sub_lists = [list_input[n:n + N] for n in range(0, len(list_input), N)]
    return sub_lists

def parse_actions_text_into_arg(text: str):
    """
    :param text: input text that needs reformatting so we are able to parse the arguments out
    :return: a list of strings, each string should be an argument
    """
    text = text.rstrip().replace("(", "").replace(")", ",").rstrip(',').replace(" ", "")
    return list(text.split(','))




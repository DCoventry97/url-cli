from shortened_url import is_shortened_url


def check_input(input_list, xml_root):
    """
    Checks the users input to see what the user wants to do and if the input is valid.
    :param input_list: comand line arguments entered when the program was called.
    :return: int value, 0 represents opening a shortened url, 1 represents shortening a new url, 2 represents help, 3
    represents renaming a shortened url, 4 represents a url to be deleted, and -1 represents an invalid input.
    """

    try:
        if is_shortened_url(input_list[1], xml_root):
            return 0

        elif input_list[1] == "-n" or input_list[1] == "--new":
            return 1

        elif input_list[1] == "-h" or input_list[1] == "--help" or input_list[1] == "help":
            return 2

        elif input_list[1] == "-r" or input_list[1] == "--rename":
            return 3

        elif input_list[1] == "-d" or input_list[1] == "--delete":
            return 4
        else:
            return -1
    except IndexError:
        print("Invalid Input: enter arguments to specify operation mode. Use help to find out more.")
        exit()


def check_new_short_is_valid(new_short):
    invalid_short_words = ["-n", "new", "help", "-h", "--help", "-r", "--rename", "-d", "--delete"]
    for word in invalid_short_words:
        if word == new_short:
            return False
    return True


def check_new_short_is_unique(new_short, root):
    for child in root:
        if child.attrib["short"] == new_short:
            return False
    return True




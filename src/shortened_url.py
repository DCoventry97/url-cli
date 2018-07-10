import xml.etree.ElementTree as ET

def is_shortened_url(shortened_url, xml_root):
    """
    Checks that the requested shortened url exists.
    :param shortened_url: A string to check for if its a valid shortened url.
    :return: boolean value for if the shortened url is valid.
    """
    for child in xml_root:
        if child.get("short") == shortened_url:
            return True
    return False


def get_url(shortened_url, xml_root):
    """
    Gets the url associated with a shortened url.
    :param shortened_url: The shortened url that is associated with a url.
    :param xml_root: The root of the xml that the url data is storied in
    :return: The url that is associated with the shortened url.
    """
    for child in xml_root:
        if child.get("short") == shortened_url:
            return child.find("url").text


def check_new_url(user_input):
    """
    Checks if the short url and url are valid.
    :param user_input: The users command line arguments when calling the program, this should be sys.argv.
    :return: A boolean for if the user input are valid.
    """
    invalid_short_words = ["-n", "new", "help", "-h", "--help", "-r", "--rename", "-d", "--delete"]
    for word in invalid_short_words:
        try:
            if word == user_input[2]:
                return False
        except IndexError:
            print("Invalid Input: specify short url and original url when making a new shortened url, use help to "
                  "find out more.")
            exit()

    if len(user_input) != 4:
        print("Invalid Input: specify a url to associate with a short url.")
        exit()

    return True


def add_url_to_xml(short_url, long_url, tree, xml_file):
    new_short_url = ET.SubElement(tree.getroot(), "shortUrl", attrib={"short": short_url})
    new_long_url = ET.SubElement(new_short_url, "url")
    new_long_url.text = long_url
    tree.write(xml_file)


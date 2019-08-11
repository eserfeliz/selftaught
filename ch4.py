def squared(number):
    """
    :param number: int
    :return:  int result of number squared
    """
    return number**2


def print_string(string):
    """
    :param string: str
    :return: str string
    """
    return "{}, is that all?".format(string)


def required_optional_params(first, second, third, fourth=4, fifth=10):
    """
    :param first: int
    :param second: int
    :param third: int
    :param fourth: int
    :param fifth: int
    :return: int sum of first, second, third, fourth and fifth vars
    """
    return first+second+third+fourth+fifth


print(required_optional_params(1, 2, 3))

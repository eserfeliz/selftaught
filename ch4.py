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


def function_one(first_num):
    """
    :param first_num: int
    :return: float quotient of first_num divided by 2
    """
    return int(first_num)/2


def function_two(second_num):
    """
    :param second_num: int
    :return:
    """
    return int(second_num)*4


def convert_str_to_float(string_to_convert):
    """
    :param string_to_convert: str
    :return:
    """
    return float(string_to_convert)


try:
    print(convert_str_to_float('a' + 1))
except (ValueError, TypeError):
    print('Invalid parameter')

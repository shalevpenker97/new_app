__author__ = 'effi'


class x(object):
    """
    this class like to suck d***
    """
    def __init__(self):
        self.__fag = "you"

    @property
    def fag(self):
        return self.__fag


def print_till_num(num):
    """
    prints all the number till num
    :param num: the paramete
    :return:
    """
    for i in range(num):
        print(i + 1)


def main():
    print_till_num(5)
    print(help(print_till_num))


if __name__ == '__main__':
    main()

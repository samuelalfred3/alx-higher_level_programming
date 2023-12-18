#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
    my_list (list): The list to print elements from.
    x (int): The number of elements of my_list to print.

    Returns:
    The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print()
    return ret

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, 5)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, 7)
print("nb_print: {:d}".format(nb_print))

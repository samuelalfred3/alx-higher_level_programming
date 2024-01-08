#!/usr/bin/python3

class MyList(list):
    """
    MyList class inherits from list.

    Public instance method:
    - def print_sorted(self): prints the list, but sorted (ascending sort).
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))

if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)
    my_list.print_sorted()
    print(my_list)

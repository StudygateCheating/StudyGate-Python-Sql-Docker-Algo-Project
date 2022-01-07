"""
1. Write a python function which returns the maximum of the absolute value of three
numbers. Include appropriate error handling.
"""


def get_max_absolute_value():
    numbers = [10, 20, -50]
    absolute_nos = []

    for number in numbers:
        try:
            absolute_nos.append(abs(number))
        except TypeError:
            raise Exception(
                "Please ensure that the list contains only numbers. They can be negative or positive"
            )

    return max(absolute_nos)


if __name__ == '__main__':
    max_value = get_max_absolute_value()
    print(max_value)

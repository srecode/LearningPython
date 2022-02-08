from traceback import print_tb


def old_mcdonald(string):
    first_half = string[:3]
    second_half = string[3:]

    return first_half.capitalize() + second_half.capitalize()

print(old_mcdonald("macdonald"))
    
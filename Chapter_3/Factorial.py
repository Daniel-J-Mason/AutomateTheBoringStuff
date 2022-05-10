def factorial(input_number):
    return_number = 1
    for i in range(input_number, 1, -1):
        return_number *= i

    return return_number


def is_tiny_ass_factorial(some_number):
    if factorial(some_number) < 200:
        print('That\'s a tiny ass factorial')
        return True
    if factorial(some_number) > 200:
        print("That's a big ass factorial")
        return False


if is_tiny_ass_factorial(5):
    print("DAMN AGAIN THAT SHITS TINY")



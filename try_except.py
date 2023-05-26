def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator

    Raises:
        ZeroDivisionError: if denominator is zero.
    '''

    try:
        fraction_val = numerator / denominator
        print(f"Fraction value is: {fraction_val}")
        return fraction_val

    except ZeroDivisionError:
        print("Denominator cannot be zero")

    return None


fractrial = divide_vals(5, 1)


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string

    Raises:
        AttributeError: if text is not a string.
    '''

    try:
        no_of_words = len(text.split())
        print(f"Number of words in string: {num_words}\n")
        return no_of_words

    except AttributeError:
        print("Text argument must be a string")

    return None


textcheck = num_words(10)

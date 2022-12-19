def get_even_from_range(min, max):
    """
    returns all even numbers from given range
    """
    for i in range(min, max):

        if i % 2 == 0:
            print(i)
        else:
            continue

get_even_from_range(1, 100)

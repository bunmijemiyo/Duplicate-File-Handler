import math  # import the required library


def calculate_cosine(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    # do not forget to round the result and print it
    print(round(math.cos(angle_in_radians), 2))
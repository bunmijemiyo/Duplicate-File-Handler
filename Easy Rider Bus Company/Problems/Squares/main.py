n = int(input())


def squares(num):
    for i in range(1, num + 1):
        yield i ** 2


# Don't forget to print out the first n numbers one by one here
for element in squares(n):
    print(element)
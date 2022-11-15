n = int(input())

def even(item):
    i = 0
    while i < item:
        yield i * 2
        i += 1


# Don't forget to print out the first n numbers one by one here
for num in even(n):
    print(num)
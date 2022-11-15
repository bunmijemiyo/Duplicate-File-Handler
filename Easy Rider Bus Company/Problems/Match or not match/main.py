import re


def matched(template, string):
    result = re.match(template, string)
    return result is not None


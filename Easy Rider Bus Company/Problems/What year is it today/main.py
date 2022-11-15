import re


# put your regex in the variable template
template = "(\\d{1,2})[./](\\d{1,2})[./](\\d{4})"
string = input()
# compare the string and the template
if re.match(template, string) is not None:
    print(re.match(template, string).group(3))
else:
    print(re.match(template, string))
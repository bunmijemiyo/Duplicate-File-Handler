import re


# put your regex in the variable template
template = "(Value|Name|Type)(Error)"
string = input()
# compare the string and the template
if re.match(template, string) is not None:
    print(re.match(template, string).group(1))
else:
    print(re.match(template, string))
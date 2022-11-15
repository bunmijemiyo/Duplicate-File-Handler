# write your code here
with open("users.json", "r") as json_dict:
    python_dict = json.load(json_dict)

print(len(python_dict["users"]))
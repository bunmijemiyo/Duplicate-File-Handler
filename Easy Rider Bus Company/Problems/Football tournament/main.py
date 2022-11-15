import itertools

# the variable 'teams' is already defined
# teams = ['Best-ever', 'Not-so-good', 'Amateurs']
for items in itertools.combinations(teams, 2):
    print(items)

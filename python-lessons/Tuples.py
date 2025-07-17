buffet_food =('ugali','rice','chapati','githeri','chai')

#showing the previous list
print("The original buffet food list included:")
for items in buffet_food:
    print(items)

#showing a modification to the list
buffet_food = ('ugali','rice','kayellow','githeri','mukimo')
print('\nModified list includes the following:')
for items in buffet_food:
    print(items.title())
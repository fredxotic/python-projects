my_fav_animes = ['bleach','attack on titan','steins gate','my hero academia','one piece','vinland saga','castlevania','hells paradise','blue lock']

friends_best_anime = my_fav_animes[:]
print(friends_best_anime)

my_fav_animes.append('tokyo ghoul')
friends_best_anime.append('dororo')

print ("My fav anime of all times include:")
for anime in my_fav_animes:
    print(anime.title())
print('\n')

print("My friend's favourite anime are:")
for anime in friends_best_anime:
    print(anime.title())
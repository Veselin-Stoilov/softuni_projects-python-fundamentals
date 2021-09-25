old_favorite = input().split(' | ')
command = input()
new_favorite = []
while not command == 'Stop!':
    if 'Join' in command:
        action, genre = command.split()
        if genre not in old_favorite:
            old_favorite.append(genre)
    elif 'Drop' in command:
        action, genre = command.split()
        if genre in old_favorite:
            old_favorite.remove(genre)
    elif 'Replace' in command:
        action, old_genre, new_genre = command.split()
        if old_genre in old_favorite:
            if new_genre not in old_favorite:
                for index, item in enumerate(old_favorite):
                    if item == old_genre:
                        old_favorite[index] = new_genre
    command = input()
new_favs = ' '.join(old_favorite)
print(new_favs)

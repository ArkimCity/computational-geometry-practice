from copy import deepcopy

num_of_people = int(input())

song_map = {i+1: [i+1] for i in range(num_of_people)}

for _ in range(int(input())):
    people =  list(map(int, input().split(' ')))[1:]
    if 1 in people:
        for person in people:
            song_map[person].append(1)
            song_map[1].append(person)
    else:
        for person in people:
            for other in people:
                temp_song = deepcopy(song_map)
                for song in temp_song[other]:
                    song_map[person].append(song)

print(1)
print(song_map)
for key in song_map:
    print(set(song_map[key]))
    if len(set(song_map[key])) == num_of_people:
        print(key)

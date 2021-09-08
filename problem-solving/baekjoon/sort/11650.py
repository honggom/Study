from sys import stdin
locations = []
for _ in range(int(stdin.readline())):
    locations.append(list(map(int, stdin.readline().split())))
[print(location[0], location[1]) for location in sorted(locations, key=lambda location:(location[0], location[1]))]

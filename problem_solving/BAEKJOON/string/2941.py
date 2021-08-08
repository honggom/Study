data = input()
ds = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for s in ds:
    data = data.replace(s, "*")

print(len(data))


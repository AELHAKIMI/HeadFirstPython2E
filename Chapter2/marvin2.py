paranoid_android = "Marvin, the paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print("\t", char)
for char in letters[-7:]:
    print("\t"*2, char)
for char in letters[12:20]:
    print("\t"*3, char)